from backend.orchestration.task_queue import task_queue

task_queue.enqueue("Discovery Agent")
task_queue.enqueue("Qualification Agent")
task_queue.enqueue("Enrichment Agent")

print(task_queue.size())

while not task_queue.is_empty():
    print(task_queue.dequeue())