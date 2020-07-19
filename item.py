from status import COMPLETED, NOT_STARTED, parseStatus

class Item:
    def __init__(self, id, title, status):
        self._id = id
        self._title = title
        self._status = parseStatus(status)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    def __str__(self):
        return f"Item(id: {self._id}, title: {self._title}, status: {self._status}"

    
    def __hash__(self):
        return hash(self._id) + hash(self._title) * 7 + hash(self._status) * 19


    def __eq__(self, other):
        return self._id == other._id and self._title == other._title and self._status == other._status 