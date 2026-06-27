from backend.orchestration.langgraph_builder import LangGraphBuilder
from backend.orchestration.workflow_state import WorkflowState

builder = LangGraphBuilder()

graph = builder.build(WorkflowState)

print(type(graph).__name__)