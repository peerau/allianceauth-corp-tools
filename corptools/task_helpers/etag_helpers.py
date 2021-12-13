from bravado.exception import HTTPNotModified
from django.core.cache import cache


MAX_ETAG_LIFE = 60*60*24*7  # 7 Days


class NotModifiedError(Exception):
    pass


def get_etag_header(operation):
    return cache.get("etag-" + operation._cache_key(), False)


def inject_etag_header(operation):
    etag = get_etag_header(operation)
    if etag:
        operation.future.request.headers["If-None-Match"] = etag


def set_etag_header(operation, headers):
    etag_key = get_etag_header(operation)
    if headers.headers.get('ETag'):
        cache.set(etag_key, headers.headers.get('ETag'), MAX_ETAG_LIFE)


def etag_results(operation, token):

    results = list()
    # override to always get the raw response for expiry header
    operation.request_config.also_return_response = True
    if token:
        operation.future.request.headers["Authorization"] = "Bearer " + \
            token.valid_access_token()
    if "page" in operation.operation.params:
        current_page = 1
        total_pages = 1
        etags_incomplete = False
        # loop all pages and add data to output array
        while current_page <= total_pages:
            operation.future.request.params["page"] = current_page
            # will use cache if applicable

            try:
                if not etags_incomplete:
                    inject_etag_header(operation)

                result, headers = operation.result()

                if get_etag_header(operation) == headers.headers.get('ETag'):
                    # if django esi is returning our cache check it manualy.
                    raise NotModifiedError()

                set_etag_header(operation, headers)

                total_pages = int(headers.headers['X-Pages'])
                # append to results list to be seamless to the client
                results += result
                current_page += 1
                etags_incomplete = True

            except (HTTPNotModified, NotModifiedError):  # etag is wrong data has changed
                if not etags_incomplete:
                    current_page += 1  # reset to page 1 and fetch everyhting
                else:
                    break
                continue
        if not etags_incomplete:
            raise NotModifiedError()

    else:  # it doesn't so just return
        inject_etag_header(operation)
        try:
            results, headers = operation.result()
        except HTTPNotModified:
            raise NotModifiedError()
        set_etag_header(operation, headers)

    return results