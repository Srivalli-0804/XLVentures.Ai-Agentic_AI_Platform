"""
Creates all database tables.
"""

from backend.database.base import Base
from backend.database.database import engine



# Import all models here
from backend.models.company import Company
from backend.models.contact import Contact
from backend.models.workflow import Workflow
# from backend.models.approval import Approval
from backend.models.agent_run import AgentRun

# Register all ORM models
import backend.models


def init_database() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)