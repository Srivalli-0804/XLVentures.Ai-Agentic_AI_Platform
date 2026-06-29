import { CompanyModel, CompanyDocument } from '../models/Company';

export type CompanyPayload = {
  name: string;
  industry: string;
  location?: string;
  website?: string;
  summary?: string;
  status?: string;
  revenue?: string;
  employees?: number;
  technologies?: string[];
  trigger?: string;
  source?: string;
  contacts?: Array<Record<string, unknown>>;
};

export const companyRepository = {
  findAll: async (): Promise<CompanyDocument[]> => {
    return CompanyModel.find().sort({ createdAt: -1 }).lean();
  },
  findById: async (id: string): Promise<CompanyDocument | null> => {
    return CompanyModel.findById(id).lean();
  },
  upsertCompanies: async (companies: CompanyPayload[]) => {
    const operations = companies.map((company) => ({
      updateOne: {
        filter: { name: company.name },
        update: { $set: company },
        upsert: true
      }
    }));

    await CompanyModel.bulkWrite(operations, { ordered: false });
  }
};
