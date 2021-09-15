import React, { useEffect, useState } from "react";
import { useQuery } from "react-query";
import Select from "react-select";
import { loadAssetLocations } from "../apis/Character";

const CharAssetLocSelect = ({ character_id, setLocation }) => {
  const [location_id, setLoc] = useState(0);
  const { isLoading, error, data } = useQuery(["asset_loc", character_id], () =>
    loadAssetLocations(character_id)
  );
  useEffect(() => {
    console.log(location_id);
    setLocation(location_id);
  });
  return (
    <Select
      isLoading={isLoading}
      options={data}
      onChange={(e) => setLoc(e.value)}
    />
  );
};

export default CharAssetLocSelect;