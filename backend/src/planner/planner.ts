import { Agent, AgentInput, AgentResult } from '../agents/Agent';
import { memoryService } from '../services/memoryService';

export interface PlannerHistoryEntry {
  agent: string;
  status: 'pending' | 'running' | 'success' | 'failed' | 'pendingApproval';
  message?: string;
  startedAt: string;
  completedAt?: string;
}

export class Planner {
  constructor(private readonly agents: Agent[]) {}

  async plan(goal: string, payload: Record<string, unknown> = {}) {
    const history: PlannerHistoryEntry[] = [];
    const input: AgentInput = { goal, payload };

    for (const agent of this.agents) {
      input.payload = await this.filterDuplicateCompanies(input.payload);

      const entry: PlannerHistoryEntry = {
        agent: agent.name,
        status: 'running',
        startedAt: new Date().toISOString()
      };

      history.push(entry);
      const result = await this.executeAgent(agent, input);

      entry.completedAt = new Date().toISOString();
      if (result.data?.approvalRequested) {
        entry.status = 'pendingApproval';
        entry.message = result.message || 'Awaiting human approval';
        await memoryService.saveEntry('plannerHistory', `${agent.name}-${entry.startedAt}`, { entry, payload: input.payload }, ['planner']);
        return { success: false, pendingApproval: true, history, output: input.payload };
      }

      if (!result.success) {
        entry.status = 'failed';
        entry.message = result.message;
        break;
      }

      entry.status = 'success';
      input.payload = { ...(input.payload || {}), ...result.data };
      await memoryService.saveEntry('plannerHistory', `${agent.name}-${entry.startedAt}`, { entry, payload: input.payload }, ['planner']);
    }

    return { success: history.every((item) => item.status === 'success'), history, output: input.payload };
  }

  private async filterDuplicateCompanies(payload: Record<string, unknown> = {}) {
    const candidates = payload.companyCandidates as Array<Record<string, unknown>> | undefined;
    if (!Array.isArray(candidates)) {
      return payload;
    }

    const uniqueCompanies: Array<Record<string, unknown>> = [];
    for (const candidate of candidates) {
      const name = String(candidate.name || '');
      if (!name) continue;
      const existing = await memoryService.findByKey('company', name);
      if (!existing) {
        uniqueCompanies.push(candidate);
      }
    }

    return { ...payload, companyCandidates: uniqueCompanies };
  }

  private async executeAgent(agent: Agent, input: AgentInput): Promise<AgentResult> {
    try {
      return await agent.execute(input);
    } catch (error) {
      return { success: false, message: (error as Error).message };
    }
  }
}
