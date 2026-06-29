import { Agent, AgentInput, AgentResult } from './Agent';

export class ValidationAgent implements Agent {
  name = 'Validation Agent';
  description = 'Validate company data and remove invalid records.';

  async execute(input: AgentInput): Promise<AgentResult> {
    const companies = (input.payload?.matchedCompanies as Array<Record<string, unknown>>)
      || [];
    const validCompanies = companies.filter((company) => Boolean(company.name && company.industry));
    return { success: true, data: { validCompanies } };
  }
}
