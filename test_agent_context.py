from backend.agents.base.agent_context import AgentContext

context = AgentContext(
    workflow_id="wf-001",
    workflow_name="Company Discovery",
)

context.set_metadata(
    "trigger_events",
    ["Funding Round"]
)

context.discovered_companies.append("OpenAI")

context.qualified_companies.append("OpenAI")

context.add_error("Sample Error")

print(context.workflow_name)

print(context.get_metadata("trigger_events"))

print(context.discovered_companies)

print(context.qualified_companies)

print(context.errors)