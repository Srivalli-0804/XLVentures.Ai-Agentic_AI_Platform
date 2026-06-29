import { connectDatabase } from '../services/database';
import { companyService } from '../services/companyService';

const seedCompanies = [
  {
    name: 'Cascade Analytics',
    industry: 'AI SaaS',
    location: 'Austin, TX',
    website: 'cascadeanalytics.ai',
    summary: 'A go-to analytics platform that delivers AI-powered forecasting and prescriptive insights for mid-market SaaS teams.',
    status: 'Prospect',
    revenue: '$18M',
    employees: 70,
    technologies: ['React', 'AWS', 'Snowflake'],
    trigger: 'Funding round',
    source: 'AI triggers'
  },
  {
    name: 'NeuralOps',
    industry: 'DevOps AI',
    location: 'London, UK',
    website: 'neuralops.ai',
    summary: 'A developer-centric AI operations platform that reduces incident toil and speeds model delivery.',
    status: 'Prospect',
    revenue: '$22M',
    employees: 95,
    technologies: ['Kubernetes', 'Python', 'Terraform'],
    trigger: 'New product launch',
    source: 'Data enrichment'
  },
  {
    name: 'Vertex Ventures',
    industry: 'Data Platform',
    location: 'San Francisco, CA',
    website: 'vertexventures.com',
    summary: 'A modern data fabric provider helping enterprises unify pipelines, analytics, and real-time AI.',
    status: 'Warm',
    revenue: '$45M',
    employees: 180,
    technologies: ['Kafka', 'Python', 'Snowflake'],
    trigger: 'Leadership change',
    source: 'Company enrichment'
  },
  {
    name: 'DatumScale',
    industry: 'Data Observability',
    location: 'New York, NY',
    website: 'datumscale.io',
    summary: 'An AI-first observability product that prevents data incidents and automates root-cause analysis.',
    status: 'Prospect',
    revenue: '$12M',
    employees: 50,
    technologies: ['Snowflake', 'dbt', 'Looker'],
    trigger: 'Customer expansion',
    source: 'Workflow output'
  }
];

async function seedData() {
  await connectDatabase();
  await companyService.saveCompanies(seedCompanies);
  console.log('Seeded sample companies.');
  process.exit(0);
}

seedData().catch((error) => {
  console.error('Error seeding data:', error);
  process.exit(1);
});
