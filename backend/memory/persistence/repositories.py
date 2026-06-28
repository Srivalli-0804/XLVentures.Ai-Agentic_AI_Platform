"""
Repository Layer

Encapsulates all database access using SQLAlchemy.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from backend.models.company import Company
from backend.models.contact import Contact
from backend.models.workflow import Workflow

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Base repository providing common CRUD operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def add(self, entity: T) -> T:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, entity: T) -> None:
        self.db.delete(entity)
        self.db.commit()


class CompanyRepository(BaseRepository[Company]):

    def get_by_id(self, company_id: int) -> Company | None:
        return self.db.get(Company, company_id)

    def get_all(self) -> list[Company]:
        return self.db.query(Company).all()


class ContactRepository(BaseRepository[Contact]):

    def get_by_id(self, contact_id: int) -> Contact | None:
        return self.db.get(Contact, contact_id)

    def get_all(self) -> list[Contact]:
        return self.db.query(Contact).all()


class WorkflowRepository(BaseRepository[Workflow]):

    def get_by_id(self, workflow_id: int) -> Workflow | None:
        return self.db.get(Workflow, workflow_id)

    def get_all(self) -> list[Workflow]:
        return self.db.query(Workflow).all()