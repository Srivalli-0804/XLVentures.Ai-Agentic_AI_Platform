from backend.memory.short_term.redis_cache import redis_cache

redis_cache.set(
    "company",
    {"name": "OpenAI"},
)

print(redis_cache.get("company"))