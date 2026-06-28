import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from agents.base.agent_registry import AgentRegistry
from agents.base.capability_router import CapabilityRouter

from agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from agents.discovery.market_signal_agent import MarketSignalAgent



def main():

    registry = AgentRegistry()

    registry.register(TriggerMonitorAgent())
    registry.register(CompanyDiscoveryAgent())
    registry.register(MarketSignalAgent())

    router = CapabilityRouter(registry)

    print("=" * 60)
    print("Testing Capability Routing")
    print("=" * 60)

    capabilities = [
        "trigger_monitor",
        "company_discovery",
        "market_signal_analysis",
    ]

    for capability in capabilities:

        agent = router.route(capability)

        print(f"{capability:<30} ---> {agent.name}")

    print()

    print("=" * 60)
    print("Capability Router Test Passed")
    print("=" * 60)


if __name__ == "__main__":
    main()