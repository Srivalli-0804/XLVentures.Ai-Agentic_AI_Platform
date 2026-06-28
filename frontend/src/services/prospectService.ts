import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api"
});

export const getProspects = async () => {
  const response = await api.get("/prospects");
  return response.data;
};

export const getWorkflowTimeline = async (
  workflowId: string
) => {
  const response = await api.get(
    `/workflows/${workflowId}/timeline`
  );

  return response.data;
};

export const getAgentTrace = async (
  workflowId: string
) => {
  const response = await api.get(
    `/workflows/${workflowId}/trace`
  );

  return response.data;
};