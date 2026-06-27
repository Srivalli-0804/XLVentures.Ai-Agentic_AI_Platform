from backend.services.workflow_service import WorkflowService

service = WorkflowService()

workflow = service.create_workflow("Company Discovery")

print(workflow.status)

workflow = service.start_workflow(workflow)

print(workflow.status)

workflow = service.complete_workflow(workflow)

print(workflow.status)