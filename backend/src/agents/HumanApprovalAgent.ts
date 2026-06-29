import { Agent, AgentInput, AgentResult } from './Agent';

export class HumanApprovalAgent implements Agent {
  name = 'Human Approval Agent';
  description = 'Pause for human review before finalizing the workflow.';

  async execute(_input: AgentInput): Promise<AgentResult> {
    return {
      success: false,
      message: 'Approval required from an admin to continue.',
      data: { approvalRequested: true }
    };
  }
}
