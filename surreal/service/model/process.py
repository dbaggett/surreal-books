import datetime as dt

class ProcessStatus(Enum):
    WAITING = "WAITING"
    IN_PROGRESS = "IN_PROGRESS"
    PUBLISHED = "PUBLISHED"

    def __str__(self):
        return self.value

class Process:
    def __init__(self, id, user_input):
        self.id = id,
        self.status = ProcessStatus.WAITING
        self.requested_at = dt.datetime.now()
        self.started_at = None
        self.finished_at = None
        self.user_input = user_input