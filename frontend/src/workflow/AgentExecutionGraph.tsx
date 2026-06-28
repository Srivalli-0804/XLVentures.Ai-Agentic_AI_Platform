import React from "react";
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  Node,
  Edge
} from "reactflow";

import "reactflow/dist/style.css";

interface AgentNode {
  id: string;
  label: string;
  status: string;
}

interface Props {
  agents: AgentNode[];
}

const statusColor = (
  status: string
) => {
  switch (status) {
    case "completed":
      return "#22c55e";

    case "running":
      return "#3b82f6";

    case "failed":
      return "#ef4444";

    default:
      return "#94a3b8";
  }
};

const AgentExecutionGraph: React.FC<Props> = ({
  agents
}) => {
  const nodes: Node[] = agents.map(
    (agent, index) => ({
      id: agent.id,

      position: {
        x: index * 250,
        y: 100
      },

      data: {
        label: (
          <div className="text-center">
            <div className="font-semibold">
              {agent.label}
            </div>

            <div
              className="mt-1 text-xs"
              style={{
                color: statusColor(
                  agent.status
                )
              }}
            >
              {agent.status}
            </div>
          </div>
        )
      },

      style: {
        width: 180,
        borderRadius: 10,
        border: `2px solid ${statusColor(
          agent.status
        )}`
      }
    })
  );

  const edges: Edge[] = [];

  for (
    let i = 0;
    i < agents.length - 1;
    i++
  ) {
    edges.push({
      id: `${i}-${i + 1}`,
      source: agents[i].id,
      target: agents[i + 1].id,
      animated: true
    });
  }

  return (
    <div
      className="bg-white rounded-lg shadow"
      style={{
        width: "100%",
        height: "500px"
      }}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
      >
        <MiniMap />

        <Controls />

        <Background />
      </ReactFlow>
    </div>
  );
};

export default AgentExecutionGraph;