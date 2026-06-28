export interface Company {
  id: string;
  company_name: string;
  domain?: string;
  industry?: string;
  employee_count?: number;
  score?: number;
  status?: string;
}

export interface Contact {
  id: string;
  company_id: string;
  first_name: string;
  last_name: string;
  title: string;
  email?: string;
  linkedin_url?: string;
  validation_status?: string;
}

export interface Recommendation {
  id: string;
  company_id: string;
  contact_id: string;
  recommendation_type: string;
  priority: string;
  message: string;
}

export interface WorkflowStep {
  id: string;
  agent_name: string;
  capability: string;
  status: "pending" | "running" | "completed" | "failed";
  started_at?: string;
  completed_at?: string;
}

export interface WorkflowRun {
  workflow_id: string;
  workflow_name: string;
  status: string;
  created_at: string;
  steps: WorkflowStep[];
}

export interface AgentTrace {
  id: string;
  agent_name: string;
  action: string;
  result: string;
  timestamp: string;
}

export interface ApprovalRequest {
  id: string;
  recommendation_id: string;
  company_name: string;
  contact_name: string;
  status: string;
  created_at: string;
}

export interface ICPConfig {
  industries: string[];
  company_sizes: string[];
  technologies: string[];
  regions: string[];
}

export interface TriggerRule {
  id: string;
  trigger_name: string;
  description: string;
  enabled: boolean;
}

export interface Persona {
  id: string;
  persona_name: string;
  title: string;
  department: string;
}

export interface AnalyticsSummary {
  discovered_companies: number;
  qualified_companies: number;
  enriched_companies: number;
  recommendations_generated: number;
  approvals_pending: number;
}