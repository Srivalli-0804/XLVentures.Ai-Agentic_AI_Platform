export interface AgentInput {
  goal: string;
  payload?: Record<string, unknown>;
}

export interface AgentResult {
  success: boolean;
  data?: Record<string, unknown>;
  message?: string;
}

export interface Agent {
  name: string;
  description: string;
  execute(input: AgentInput): Promise<AgentResult>;
}
