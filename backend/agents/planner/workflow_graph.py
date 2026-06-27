from __future__ import annotations

import logging
from collections import deque
from typing import Dict, List

from .workflow_models import WorkflowDefinition, WorkflowNode

logger = logging.getLogger(__name__)


class WorkflowGraph:
    """
    Central registry and manager for all workflows.

    Responsibilities:
        - Register workflows
        - Validate workflow structure
        - Retrieve workflows
        - Generate execution order

    The graph stores workflow definitions only.
    It never executes agents.
    """

    def __init__(self) -> None:
        self._workflows: Dict[str, WorkflowDefinition] = {}

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def register_workflow(
        self,
        workflow: WorkflowDefinition,
    ) -> None:
        """
        Register a new workflow.

        Raises:
            ValueError
                if workflow already exists.
        """

        if workflow.name in self._workflows:
            raise ValueError(
                f"Workflow '{workflow.name}' already registered."
            )

        self.validate_workflow(workflow)

        self._workflows[workflow.name] = workflow

        logger.info(
            "Registered workflow '%s'",
            workflow.name,
        )

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def get_workflow(
        self,
        workflow_name: str,
    ) -> WorkflowDefinition:
        """
        Returns a workflow.

        Raises:
            LookupError
                if workflow is not found.
        """

        workflow = self._workflows.get(workflow_name)

        if workflow is None:
            raise LookupError(
                f"Workflow '{workflow_name}' not found."
            )

        return workflow

    def list_workflows(self) -> List[str]:
        """
        Returns all registered workflow names.
        """

        return sorted(self._workflows.keys())

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate_workflow(
        self,
        workflow: WorkflowDefinition,
    ) -> None:
        """
        Performs basic validation.

        Checks:

        - start node exists
        - every dependency exists
        - every next node exists
        """

        if workflow.start_node not in workflow.nodes:
            raise ValueError(
                f"Start node '{workflow.start_node}' not found."
            )

        for node in workflow.nodes.values():

            for dependency in node.dependencies:

                if dependency not in workflow.nodes:
                    raise ValueError(
                        f"Dependency '{dependency}' "
                        f"does not exist."
                    )

            for next_node in node.next_nodes:

                if next_node not in workflow.nodes:
                    raise ValueError(
                        f"Next node '{next_node}' "
                        f"does not exist."
                    )

    # ---------------------------------------------------------
    # Execution Planning
    # ---------------------------------------------------------

    def build_execution_plan(
        self,
        workflow_name: str,
    ) -> List[WorkflowNode]:
        """
        Returns workflow nodes
        in execution order.

        Uses Breadth-First Traversal.
        """

        workflow = self.get_workflow(workflow_name)

        visited = set()

        queue = deque([workflow.start_node])

        execution_plan: List[WorkflowNode] = []

        while queue:

            node_id = queue.popleft()

            if node_id in visited:
                continue

            visited.add(node_id)

            node = workflow.get_node(node_id)

            execution_plan.append(node)

            for next_node in node.next_nodes:
                queue.append(next_node)

        return execution_plan

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def remove_workflow(
        self,
        workflow_name: str,
    ) -> None:

        self._workflows.pop(workflow_name, None)

    def contains(
        self,
        workflow_name: str,
    ) -> bool:

        return workflow_name in self._workflows

    def __len__(self) -> int:

        return len(self._workflows)