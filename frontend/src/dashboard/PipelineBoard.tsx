import React from "react";
import ProspectCard, { Prospect } from "./ProspectCard";

interface Props {
  prospects: Prospect[];
}

const PipelineBoard: React.FC<Props> = ({ prospects }) => {
  const columns = [
    "Discovered",
    "Qualified",
    "Enriched",
    "Recommended"
  ];

  return (
    <div className="grid grid-cols-4 gap-4">
      {columns.map((column) => (
        <div
          key={column}
          className="bg-gray-100 rounded-lg p-4"
        >
          <h2 className="font-bold mb-4">
            {column}
          </h2>

          <div className="space-y-3">
            {prospects
              .filter((p) => p.status === column)
              .map((prospect) => (
                <ProspectCard
                  key={prospect.id}
                  prospect={prospect}
                />
              ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default PipelineBoard;