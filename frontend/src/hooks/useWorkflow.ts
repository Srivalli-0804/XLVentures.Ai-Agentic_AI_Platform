import { useEffect } from "react";

import { useWorkflowStore } from "../store/workflowStore";

export const useWorkflow = (
  workflowId?: string
) => {
  const {
    workflows,
    timeline,
    traces,
    loading,
    error,

    fetchWorkflows,
    fetchTimeline,
    fetchTrace,

    runWorkflow,
    selectedWorkflow,
    setSelectedWorkflow
  } = useWorkflowStore();

  useEffect(() => {
    fetchWorkflows();
  }, []);

  useEffect(() => {
    if (workflowId) {
      fetchTimeline(workflowId);
      fetchTrace(workflowId);
    }
  }, [workflowId]);

  return {
    workflows,
    timeline,
    traces,

    loading,
    error,

    runWorkflow,

    selectedWorkflow,
    setSelectedWorkflow,

    fetchTimeline,
    fetchTrace,
    fetchWorkflows
  };
};