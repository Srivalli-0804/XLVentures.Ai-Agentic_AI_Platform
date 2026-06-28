from backend.tools.base.register_tools import register_all_tools

from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.discovery.company_discovery_agent import (
    CompanyDiscoveryAgent,
)

from backend.agents.base.agent_context import AgentContext

register_all_tools()

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Discovery",
)

trigger = TriggerMonitorAgent()
discovery = CompanyDiscoveryAgent()

context = trigger.execute(context)
context = discovery.execute(context)

print(context.get_metadata("trigger_events"))
print()
print(context.discovered_companies)