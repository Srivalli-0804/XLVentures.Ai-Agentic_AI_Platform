import React from "react";

export interface Prospect {
  id: string;
  company_name: string;
  score: number;
  industry: string;
  status: string;
}

interface Props {
  prospect: Prospect;
}

const ProspectCard: React.FC<Props> = ({ prospect }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-4 border">
      <div className="flex justify-between items-center">
        <h3 className="font-semibold text-lg">
          {prospect.company_name}
        </h3>

        <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded">
          {prospect.score}
        </span>
      </div>

      <p className="text-gray-600 mt-2">
        {prospect.industry}
      </p>

      <div className="mt-3">
        <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
          {prospect.status}
        </span>
      </div>
    </div>
  );
};

export default ProspectCard;