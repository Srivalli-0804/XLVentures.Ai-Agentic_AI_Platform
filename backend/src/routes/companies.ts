import { Router } from 'express';
import { getCompanies, getCompanyById } from '../controllers/companyController';

export const companiesRouter = Router();

companiesRouter.get('/', getCompanies);
companiesRouter.get('/:id', getCompanyById);
