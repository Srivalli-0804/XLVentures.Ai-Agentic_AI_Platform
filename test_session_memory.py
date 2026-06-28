from backend.memory.short_term.session_memory import session_memory

workflow_id = "wf-001"

session_memory.save(
    workflow_id,
    {
        "status": "RUNNING",
        "companies": [
            "Microsoft",
            "Google",
            "Amazon"
        ],
    },
)

print(session_memory.load(workflow_id))

print(session_memory.exists(workflow_id))

session_memory.delete(workflow_id)

print(session_memory.exists(workflow_id))