import { Request, Response, NextFunction } from 'express';
import { companyService } from '../services/companyService';

export const getCompanies = async (_req: Request, res: Response, next: NextFunction) => {
  try {
    const companies = await companyService.listCompanies();
    res.json(companies);
  } catch (error) {
    next(error);
  }
};

export const getCompanyById = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { id } = req.params;
    const company = await companyService.getCompanyById(id);
    if (!company) {
      return res.status(404).json({ message: 'Company not found' });
    }
    res.json(company);
  } catch (error) {
    next(error);
  }
};
