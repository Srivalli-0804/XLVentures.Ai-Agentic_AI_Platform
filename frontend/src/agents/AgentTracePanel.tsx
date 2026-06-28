import React from "react";

export interface AgentTrace {
  id: string;
  agent_name: string;
  action: string;
  result: string;
}

interface Props {
  traces: AgentTrace[];
}

const AgentTracePanel: React.FC<Props> = ({
  traces
}) => {
  return (
    <div className="bg-white rounded-lg shadow p-4">
      <h2 className="text-xl font-bold mb-4">
        Agent Trace
      </h2>

      <div className="space-y-3">
        {traces.map((trace) => (
          <div
            key={trace.id}
            className="border rounded p-3"
          >
            <h3 className="font-semibold">
              {trace.agent_name}
            </h3>

            <p className="text-sm">
              {trace.action}
            </p>

            <p className="text-green-600 text-sm mt-1">
              {trace.result}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentTracePanel;