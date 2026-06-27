# ProspectIQ Orchestration Architecture

## Purpose

The orchestration layer coordinates workflow execution across planners, execution engines,
business agents, memory, and persistence.

It contains no business logic.

Its responsibility is to execute workflows reliably.

---

# Architecture

User

↓

FastAPI

↓

Workflow Service

↓

Planner Agent

↓

Workflow Graph

↓

Execution Plan

↓

LangGraph Builder

↓

Workflow State

↓

Execution Engine

↓

Task Queue

↓

Capability Router

↓

Business Agents

↓

Agent Context

↓

Memory

↓

Database

---

# Component Responsibilities

## Planner

Responsibilities

- Decide execution plan
- Generate workflow graph
- Never execute agents
- Never call tools

Input

User Request

Output

ExecutionPlan

---

## Workflow Graph

Responsibilities

Represents workflow as a DAG.

Contains

WorkflowNode

WorkflowEdge

Dependencies

Execution order

---

## LangGraph Builder

Responsibilities

Convert WorkflowGraph

↓

LangGraph StateGraph

Never contains business logic.

Never contains planning logic.

---

## Workflow State

WorkflowState is the runtime state of an executing workflow.

It is shared across the entire execution.

Fields

workflow_id

workflow_name

status

current_step

execution_plan

planner_output

agent_context

shared_memory

results

errors

started_at

completed_at

---

## Execution Engine

Responsibilities

Execute execution plan.

Never decide workflow.

Never perform business logic.

Only execute.

---

## Task Queue

Responsibilities

Schedule tasks.

Supports

Sequential execution

Parallel execution

Retries

Future support

Celery

Redis Queue

RabbitMQ

Kafka

---

## Event Bus

Responsibilities

Publish events.

Examples

WorkflowStarted

WorkflowCompleted

AgentStarted

AgentCompleted

CompanyDiscovered

RecommendationGenerated

ApprovalRequested

ApprovalCompleted

---

## Capability Router

Responsibilities

Route capability

↓

Correct business agent

Never execute workflow.

---

## Business Agents

Responsibilities

Business logic only.

Read AgentContext.

Update AgentContext.

Never communicate directly.

Never instantiate another agent.

---

## Agent Context

Shared communication object.

Contains

metadata

companies

contacts

recommendations

approvals

planner_output

Every agent reads

↓

AgentContext

Every agent writes

↓

AgentContext

---

## Memory

Responsibilities

Short-term memory

Session memory

Long-term memory

Semantic memory

Vector search

---

## Database

Responsibilities

Persistence only.

Stores

Companies

Contacts

Workflow

Approval

Agent Runs

---

# Workflow Lifecycle

User

↓

Planner

↓

Execution Plan

↓

Workflow State

↓

Execution Engine

↓

Task Queue

↓

Business Agents

↓

Agent Context updated

↓

Workflow State updated

↓

Database persisted

↓

Workflow completed

---

# Design Principles

Planner decides.

Execution Engine executes.

Business Agents perform business logic.

Workflow State stores runtime state.

Memory stores shared knowledge.

Database stores persistent records.

Never violate these boundaries.