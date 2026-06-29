import { companyRepository, CompanyPayload } from '../repositories/companyRepository';

export const companyService = {
  listCompanies: async () => companyRepository.findAll(),
  getCompanyById: async (id: string) => companyRepository.findById(id),
  saveCompanies: async (companies: CompanyPayload[]) => companyRepository.upsertCompanies(companies)
};
