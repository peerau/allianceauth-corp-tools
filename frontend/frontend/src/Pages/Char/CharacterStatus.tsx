import CharacterStatusPanels from "../../Components/Character/CharacterStatusPanels";
import CharacterStatusTable from "../../Components/Character/CharacterStatusTable";
import { loadCharacterStatus } from "../../api/character";
import { useState } from "react";
import { Card, Form, Row } from "react-bootstrap";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";

const CharacterStatus = () => {
  const { characterID } = useParams();
  const [table, setTable] = useState(false);
  const { data, isFetching } = useQuery({
    queryKey: ["status", characterID],
    queryFn: () => loadCharacterStatus(characterID),
    refetchOnWindowFocus: false,
    initialData: { characters: [], main: undefined, headers: [] },
  });

  return (
    <>
      <Card.Header className="text-end">
        <div className="d-flex justify-content-end">
          <Form.Check // prettier-ignore
            type="switch"
            id="custom-switch"
            label="Display in Table Format"
            onChange={(event) => {
              setTable(event.target.checked);
            }}
            defaultChecked={table}
          />
        </div>
      </Card.Header>
      {table ? (
        <CharacterStatusTable {...{ isFetching }} data={data} />
      ) : (
        <CharacterStatusPanels {...{ isFetching }} data={data} />
      )}
    </>
  );
};

export default CharacterStatus;
