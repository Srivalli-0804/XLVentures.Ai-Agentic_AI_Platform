from backend.tools.base.register_tools import register_all_tools

from backend.agents.base.agent_context import AgentContext

from backend.agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from backend.agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from backend.agents.qualification.icp_qualifier_agent import ICPQualifierAgent
from backend.agents.scoring.company_scoring_agent import CompanyScoringAgent

register_all_tools()

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Prospect Discovery",
)

trigger = TriggerMonitorAgent()
discovery = CompanyDiscoveryAgent()
qualifier = ICPQualifierAgent()
scorer = CompanyScoringAgent()

context = trigger.execute(context)
context = discovery.execute(context)
context = qualifier.execute(context)
context = scorer.execute(context)

print("Scored Companies:")
print(context.scored_companies)