from backend.agents.planner.planner_agent import PlannerAgent

planner = PlannerAgent()

plan = planner.create_execution_plan()

for node in plan:
    print(node.capability)