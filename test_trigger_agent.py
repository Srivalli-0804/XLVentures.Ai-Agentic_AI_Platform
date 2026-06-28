from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.base.agent_context import AgentContext

agent = TriggerMonitorAgent()

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Discovery",
)

context = agent.execute(context)

print(context.get_metadata("trigger_events"))