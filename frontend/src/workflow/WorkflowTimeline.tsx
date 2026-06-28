import React from "react";

export interface WorkflowStep {
  id: string;
  agent: string;
  status: string;
  timestamp: string;
}

interface Props {
  steps: WorkflowStep[];
}

const WorkflowTimeline: React.FC<Props> = ({
  steps
}) => {
  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-4">
        Workflow Timeline
      </h2>

      <div className="space-y-4">
        {steps.map((step) => (
          <div
            key={step.id}
            className="border-l-4 border-blue-500 pl-4"
          >
            <h3 className="font-semibold">
              {step.agent}
            </h3>

            <p className="text-sm text-gray-500">
              {step.timestamp}
            </p>

            <span className="text-blue-600 text-sm">
              {step.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WorkflowTimeline;