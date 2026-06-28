from backend.agents.base.base_agent import BaseAgent
from backend.agents.base.agent_context import AgentContext


class DummyAgent(BaseAgent):

    capability = "dummy"

    def validate(self, context):
        print("Validate")

    def _run(self, context):
        print("Run")
        context.set_metadata("executed", True)
        return context


context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Demo",
)

agent = DummyAgent()

context = agent.execute(context)

print(context.get_metadata("executed"))