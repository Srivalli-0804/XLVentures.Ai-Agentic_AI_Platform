# Force SQLAlchemy to register all ORM models
import backend.models.company
import backend.models.contact
import backend.models.workflow
import backend.models.agent_run

from backend.database.session import SessionLocal
from backend.memory.persistence.repositories import CompanyRepository

db = SessionLocal()

repo = CompanyRepository(db)

print(repo.get_all())

db.close()