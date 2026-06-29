import api from './authApi';

export type DashboardStats = {
  workflows: number;
  companies: number;
  agents: number;
  memory: number;
  plannerStatus: string;
  recentWorkflows: Array<{ id: string; name: string; status: string }>;
};

export type Company = {
  _id: string;
  name: string;
  industry?: string;
  location?: string;
  website?: string;
  summary?: string;
  status?: string;
  revenue?: string;
  employees?: number;
  technologies?: string[];
  trigger?: string;
  source?: string;
  contacts?: Array<Record<string, unknown>>;
};

export const fetchDashboardStats = async (): Promise<DashboardStats> => {
  const response = await api.get<DashboardStats>('/stats');
  return response.data;
};

export const fetchCompanies = async (): Promise<Company[]> => {
  const response = await api.get<Company[]>('/companies');
  return response.data;
};

export const fetchCompanyDetails = async (id: string): Promise<Company> => {
  const response = await api.get<Company>(`/company/${id}`);
  return response.data;
};

export type WorkflowRun = {
  _id: string;
  name: string;
  status: string;
  steps: Array<{ agent: string; status: string; message?: string }>;
  createdAt: string;
};

export type MemoryEntry = {
  _id: string;
  type: string;
  key: string;
  payload: Record<string, unknown>;
  tags: string[];
  updatedAt: string;
};

export type AgentInfo = {
  name: string;
  description: string;
};

export type WorkflowQueueResponse = {
  jobId: string;
  workflowId: string;
};

export type UserProfile = {
  email: string;
  role: string;
};

export const fetchWorkflowStatus = async (): Promise<WorkflowRun[]> => {
  const response = await api.get<WorkflowRun[]>('/workflow/status');
  return response.data;
};

export const approveWorkflow = async (workflowId: string, action: 'approve' | 'reject') => {
  const response = await api.post('/workflow/approve', { workflowId, action });
  return response.data;
};

export const fetchMemoryEntries = async (): Promise<MemoryEntry[]> => {
  const response = await api.get<MemoryEntry[]>('/memory');
  return response.data;
};

export const fetchAgents = async (): Promise<AgentInfo[]> => {
  const response = await api.get<AgentInfo[]>('/agents');
  return response.data;
};

export const queueWorkflow = async (goal: string, payload = {}): Promise<WorkflowQueueResponse> => {
  const response = await api.post<WorkflowQueueResponse>('/workflow/queue/run', { goal, payload });
  return response.data;
};

export const fetchUserProfile = async (): Promise<UserProfile> => {
  const response = await api.get<UserProfile>('/auth/me');
  return response.data;
};

export const loginRequest = async (email: string, password: string) => {
  const response = await api.post('/auth/login', { email, password });
  return response.data;
};
