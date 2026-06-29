import { MonitorAgent } from './MonitorAgent';
import { ICPMatchingAgent } from './ICPMatchingAgent';
import { ValidationAgent } from './ValidationAgent';
import { CompanyEnrichmentAgent } from './CompanyEnrichmentAgent';
import { PersonaFinderAgent } from './PersonaFinderAgent';
import { ContactEnrichmentAgent } from './ContactEnrichmentAgent';
import { RecommendationAgent } from './RecommendationAgent';
import { HumanApprovalAgent } from './HumanApprovalAgent';
import { ExportAgent } from './ExportAgent';

export const agents = [
  new MonitorAgent(),
  new ICPMatchingAgent(),
  new ValidationAgent(),
  new CompanyEnrichmentAgent(),
  new PersonaFinderAgent(),
  new ContactEnrichmentAgent(),
  new RecommendationAgent(),
  new HumanApprovalAgent(),
  new ExportAgent()
];
