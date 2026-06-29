import { Agent, AgentInput, AgentResult } from './Agent';

export class RecommendationAgent implements Agent {
  name = 'Recommendation Agent';
  description = 'Generate action-oriented recommendations for the prospect list.';

  async execute(input: AgentInput): Promise<AgentResult> {
    const companies = (input.payload?.enrichedCompanies as Array<Record<string, unknown>>)
      || [];
    const recommendations = companies.map((company) => ({
      company: company.name,
      recommendation: `Reach out to the CTO at ${company.website} with a narrative about data-driven AI scaling.`
    }));

    return { success: true, data: { recommendations } };
  }
}
