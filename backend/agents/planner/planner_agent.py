from __future__ import annotations

import logging

from ..base.agent_context import AgentContext
from .execution_engine import ExecutionEngine
from .execution_plan import ExecutionPlan
from .planning_strategy import PlanningStrategy
from .workflow_graph import WorkflowGraph


logger = logging.getLogger(__name__)


class PlannerAgent:
    """
    PlannerAgent is the brain of the platform.

    Responsibilities
    ----------------
    1. Determine which workflow should execute.
    2. Build an execution plan.
    3. Delegate execution to the ExecutionEngine.
    4. Return the updated AgentContext.

    The Planner never executes business logic directly.
    """

    def __init__(
        self,
        planning_strategy: PlanningStrategy,
        workflow_graph: WorkflowGraph,
        execution_engine: ExecutionEngine,
    ) -> None:

        self.strategy = planning_strategy
        self.workflow_graph = workflow_graph
        self.execution_engine = execution_engine

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    async def execute(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Executes the complete planning lifecycle.

        Parameters
        ----------
        context:
            Shared AgentContext.

        Returns
        -------
        AgentContext
            Updated context after workflow execution.
        """

        logger.info("Planner started.")

        # -----------------------------------------------------
        # Step 1 : Determine workflow
        # -----------------------------------------------------

        workflow_name = await self.strategy.plan(context)

        logger.info(
            "Selected workflow: %s",
            workflow_name,
        )

        # -----------------------------------------------------
        # Step 2 : Build execution plan
        # -----------------------------------------------------

        workflow = self.workflow_graph.get_workflow(
            workflow_name
        )

        workflow_nodes = self.workflow_graph.build_execution_plan(
            workflow_name
        )

        execution_plan = ExecutionPlan(
            workflow_name=workflow.name,
            workflow_version=workflow.version,
            steps=workflow_nodes,
        )

        logger.info(
            "Execution plan created (%d steps).",
            execution_plan.total_steps(),
        )

        # -----------------------------------------------------
        # Step 3 : Execute workflow
        # -----------------------------------------------------

        updated_context = await self.execution_engine.execute_plan(
            execution_plan,
            context,
        )

        logger.info("Planner completed successfully.")

        return updated_context