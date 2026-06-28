from backend.orchestration.event_bus import event_bus
from backend.orchestration.events.event import Event
from backend.orchestration.events.event_types import EventType


def workflow_started(event: Event):

    print("Workflow Started")

    print(event.payload)


event_bus.subscribe(
    EventType.WORKFLOW_STARTED,
    workflow_started,
)

event_bus.publish(
    Event(
        event_type=EventType.WORKFLOW_STARTED,
        payload={
            "workflow": "Company Discovery"
        },
    )
)