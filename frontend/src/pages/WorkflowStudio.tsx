import React from "react";

import AgentExecutionGraph from "../workflow/AgentExecutionGraph";
import PlannerDecisionPanel from "../workflow/PlannerDecisionPanel";

const WorkflowStudio = () => {
  const agents = [
    {
      id: "1",
      label: "TriggerMonitorAgent",
      status: "completed"
    },
    {
      id: "2",
      label: "CompanyDiscoveryAgent",
      status: "completed"
    },
    {
      id: "3",
      label: "ICPQualifierAgent",
      status: "running"
    }
  ];

  const decisions = [
    {
      id: "1",
      capability: "company_discovery",
      selectedAgent:
        "CompanyDiscoveryAgent",
      reason:
        "Best capability match for discovery.",
      timestamp:
        new Date().toISOString()
    }
  ];

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">
        Workflow Studio
      </h1>

      <AgentExecutionGraph
        agents={agents}
      />

      <PlannerDecisionPanel
        decisions={decisions}
      />
    </div>
  );
};

export default WorkflowStudio;