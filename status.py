NOT_STARTED = 'Not Started'
COMPLETED = 'Completed'

def parseStatus(status):
    if not status in [NOT_STARTED, COMPLETED]:
        raise TypeError(f"Invalid status: {status}")
    return status