import { MemoryEntryModel, MemoryEntryDocument, MemoryEntryType } from '../models/MemoryEntry';

export const memoryService = {
  saveEntry: async (type: MemoryEntryType, key: string, payload: Record<string, unknown>, tags: string[]) => {
    const existing = await MemoryEntryModel.findOne({ type, key });
    if (existing) {
      existing.payload = payload;
      existing.tags = Array.from(new Set([...existing.tags, ...tags]));
      return existing.save();
    }

    return MemoryEntryModel.create({ type, key, payload, tags });
  },
  getEntries: async () => MemoryEntryModel.find().sort({ updatedAt: -1 }).lean(),
  findByKey: async (type: MemoryEntryType, key: string) => MemoryEntryModel.findOne({ type, key }).lean()
};
