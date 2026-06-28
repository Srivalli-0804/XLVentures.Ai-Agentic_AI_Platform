import React, {
  useEffect,
  useState
} from "react";

import PipelineBoard from "../dashboard/PipelineBoard";
import WorkflowTimeline from "../workflow/WorkflowTimeline";
import AgentTracePanel from "../agents/AgentTracePanel";

import {
  getProspects,
  getWorkflowTimeline,
  getAgentTrace
} from "../services/prospectService";

const Dashboard = () => {
  const [prospects, setProspects] =
    useState<any[]>([]);

  const [timeline, setTimeline] =
    useState<any[]>([]);

  const [traces, setTraces] =
    useState<any[]>([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const prospectData =
        await getProspects();

      const timelineData =
        await getWorkflowTimeline(
          "demo-workflow"
        );

      const traceData =
        await getAgentTrace(
          "demo-workflow"
        );

      setProspects(prospectData);
      setTimeline(timelineData);
      setTraces(traceData);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="p-6 space-y-8">
      <PipelineBoard prospects={prospects} />

      <WorkflowTimeline
        steps={timeline}
      />

      <AgentTracePanel
        traces={traces}
      />
    </div>
  );
};

export default Dashboard;