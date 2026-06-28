import { create } from "zustand";
import api from "../lib/api";

import {
  WorkflowRun,
  WorkflowStep,
  AgentTrace
} from "../lib/types";

interface WorkflowState {
  workflows: WorkflowRun[];

  timeline: WorkflowStep[];

  traces: AgentTrace[];

  selectedWorkflow:
    | string
    | null;

  loading: boolean;

  error: string | null;

  fetchWorkflows: () => Promise<void>;

  fetchTimeline: (
    workflowId: string
  ) => Promise<void>;

  fetchTrace: (
    workflowId: string
  ) => Promise<void>;

  setSelectedWorkflow: (
    workflowId: string
  ) => void;

  runWorkflow: (
    workflowName: string
  ) => Promise<void>;
}

export const useWorkflowStore =
  create<WorkflowState>(
    (set) => ({
      workflows: [],
      timeline: [],
      traces: [],

      selectedWorkflow:
        null,

      loading: false,
      error: null,

      fetchWorkflows:
        async () => {
          try {
            set({
              loading: true
            });

            const response =
              await api.get(
                "/workflows"
              );

            set({
              workflows:
                response.data,
              loading: false
            });
          } catch (error: any) {
            set({
              loading: false,
              error:
                error.message
            });
          }
        },

      fetchTimeline:
        async (
          workflowId: string
        ) => {
          try {
            const response =
              await api.get(
                `/workflows/${workflowId}/timeline`
              );

            set({
              timeline:
                response.data
            });
          } catch (error: any) {
            set({
              error:
                error.message
            });
          }
        },

      fetchTrace:
        async (
          workflowId: string
        ) => {
          try {
            const response =
              await api.get(
                `/workflows/${workflowId}/trace`
              );

            set({
              traces:
                response.data
            });
          } catch (error: any) {
            set({
              error:
                error.message
            });
          }
        },

      setSelectedWorkflow:
        (
          workflowId: string
        ) =>
          set({
            selectedWorkflow:
              workflowId
          }),

      runWorkflow:
        async (
          workflowName: string
        ) => {
          try {
            set({
              loading: true
            });

            await api.post(
              "/workflows/run",
              {
                workflow_name:
                  workflowName
              }
            );

            set({
              loading: false
            });
          } catch (error: any) {
            set({
              loading: false,
              error:
                error.message
            });
          }
        }
    })
  );