from backend.agents.base.agent_registry import agent_registry


class DummyAgent:
    pass


agent_registry.register(
    "company_discovery",
    DummyAgent(),
)

print(agent_registry.exists("company_discovery"))

print(agent_registry.capabilities())

print(agent_registry.get("company_discovery"))

agent_registry.unregister("company_discovery")

print(agent_registry.exists("company_discovery"))