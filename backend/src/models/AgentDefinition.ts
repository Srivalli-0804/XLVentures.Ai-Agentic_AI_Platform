export type AgentStatus = 'idle' | 'running' | 'success' | 'failed' | 'waiting';

export interface AgentDefinition {
  name: string;
  description: string;
  status: AgentStatus;
}
