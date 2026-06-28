from backend.tools.base.register_tools import register_all_tools

from backend.agents.base.agent_context import AgentContext

from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from backend.agents.qualification.icp_qualifier_agent import (
    ICPQualifierAgent,
)

register_all_tools()

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Prospect Discovery",
)

trigger = TriggerMonitorAgent()
discovery = CompanyDiscoveryAgent()
qualifier = ICPQualifierAgent()

context = trigger.execute(context)
context = discovery.execute(context)
context = qualifier.execute(context)

print("Qualified Companies:")
print(context.qualified_companies)