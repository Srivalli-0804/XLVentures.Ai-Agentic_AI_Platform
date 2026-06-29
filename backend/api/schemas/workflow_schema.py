from __future__ import annotations

from pydantic import BaseModel


class CreateWorkflowRequest(BaseModel):
    workflow_name: str

