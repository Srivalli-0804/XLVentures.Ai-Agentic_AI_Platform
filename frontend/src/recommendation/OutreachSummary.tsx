import React from "react";

interface SummaryData {
  totalRecommendations: number;
  highPriority: number;
  mediumPriority: number;
  lowPriority: number;
}

interface Props {
  summary: SummaryData;
}

const OutreachSummary: React.FC<Props> = ({
  summary
}) => {
  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-5">
        Outreach Summary
      </h2>

      <div className="grid grid-cols-4 gap-4">
        <div className="bg-blue-50 rounded-lg p-4">
          <div className="text-sm text-gray-500">
            Total
          </div>

          <div className="text-2xl font-bold">
            {
              summary.totalRecommendations
            }
          </div>
        </div>

        <div className="bg-red-50 rounded-lg p-4">
          <div className="text-sm text-gray-500">
            High Priority
          </div>

          <div className="text-2xl font-bold">
            {summary.highPriority}
          </div>
        </div>

        <div className="bg-yellow-50 rounded-lg p-4">
          <div className="text-sm text-gray-500">
            Medium Priority
          </div>

          <div className="text-2xl font-bold">
            {summary.mediumPriority}
          </div>
        </div>

        <div className="bg-green-50 rounded-lg p-4">
          <div className="text-sm text-gray-500">
            Low Priority
          </div>

          <div className="text-2xl font-bold">
            {summary.lowPriority}
          </div>
        </div>
      </div>
    </div>
  );
};

export default OutreachSummary;