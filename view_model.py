from status import COMPLETED, IN_PROGRESS, NOT_STARTED

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def not_started_items(self):
        return self.get_items_with_status(NOT_STARTED)

    @property
    def in_progress_items(self):
        return self.get_items_with_status(IN_PROGRESS)

    @property
    def completed_items(self):
        return self.get_items_with_status(COMPLETED)

    def get_items_with_status(self, status):
        return list(filter(lambda item: item.status == status, self.items))