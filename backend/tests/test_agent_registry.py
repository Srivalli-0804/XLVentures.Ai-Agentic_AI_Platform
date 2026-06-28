from agents.base.agent_registry import AgentRegistry

from agents.discovery.trigger_monitor_agent import TriggerMonitorAgent
from agents.discovery.company_discovery_agent import CompanyDiscoveryAgent
from agents.discovery.market_signal_agent import MarketSignalAgent
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


def main():

    registry = AgentRegistry()

    print("=" * 60)
    print("Registering Agents")
    print("=" * 60)

    registry.register(TriggerMonitorAgent())
    registry.register(CompanyDiscoveryAgent())
    registry.register(MarketSignalAgent())

    print("Registered Successfully\n")

    print("=" * 60)
    print("Registered Agent Names")
    print("=" * 60)

    for agent_name in registry.get_registered_agent_names():
        print(agent_name)

    print()

    print("=" * 60)
    print("Retrieving Agent")
    print("=" * 60)

    agent = registry.get_agent("Trigger Monitor Agent")

    print(agent)

    print()

    print("=" * 60)
    print("Registry Size")
    print("=" * 60)

    print(len(registry))

    print()

    print("=" * 60)
    print("Test Passed")
    print("=" * 60)


if __name__ == "__main__":
    main()