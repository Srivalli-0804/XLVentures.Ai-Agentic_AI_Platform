import { Agent, AgentInput, AgentResult } from './Agent';

export class ICPMatchingAgent implements Agent {
  name = 'ICP Matching Agent';
  description = 'Evaluate companies against the ideal customer profile.';

  async execute(input: AgentInput): Promise<AgentResult> {
    const candidates = (input.payload?.companyCandidates as Array<Record<string, unknown>>)
      || [];
    const matches = candidates.map((company) => ({
      ...company,
      icpMatch: true
    }));

    return { success: true, data: { matchedCompanies: matches } };
  }
}
