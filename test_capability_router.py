from backend.agents.base.agent_registry import agent_registry
from backend.agents.base.capability_router import capability_router


class DiscoveryAgent:
    def execute(self):
        print("Discovery Agent Executed")


agent_registry.register(
    "company_discovery",
    DiscoveryAgent(),
)

print(capability_router.can_resolve("company_discovery"))

agent = capability_router.resolve("company_discovery")

agent.execute()

print(capability_router.available_capabilities())