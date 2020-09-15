NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'

STATUSES = [NOT_STARTED, IN_PROGRESS, COMPLETED]

def parseStatus(status):
    if not status in STATUSES:
        raise TypeError(f"Invalid status: {status}")
    return status