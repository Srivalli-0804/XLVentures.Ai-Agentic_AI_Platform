import React from "react";

export interface PlannerDecision {
  id: string;

  capability: string;

  selectedAgent: string;

  reason: string;

  timestamp: string;
}

interface Props {
  decisions: PlannerDecision[];
}

const PlannerDecisionPanel: React.FC<Props> = ({
  decisions
}) => {
  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-5">
        Planner Decisions
      </h2>

      <div className="space-y-4">
        {decisions.map(
          (decision) => (
            <div
              key={decision.id}
              className="border rounded-lg p-4"
            >
              <div className="flex justify-between">
                <h3 className="font-semibold">
                  {
                    decision.capability
                  }
                </h3>

                <span className="text-sm text-gray-500">
                  {
                    decision.timestamp
                  }
                </span>
              </div>

              <div className="mt-2">
                <span className="font-medium">
                  Selected Agent:
                </span>{" "}
                {
                  decision.selectedAgent
                }
              </div>

              <div className="mt-2 text-gray-700">
                {decision.reason}
              </div>
            </div>
          )
        )}
      </div>
    </div>
  );
};

export default PlannerDecisionPanel;