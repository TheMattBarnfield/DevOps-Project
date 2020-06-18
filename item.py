from status import COMPLETED, parseStatus

class Item:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = parseStatus(status)


    def is_completed(self):
        return self.status == COMPLETED


    def __str__(self):
        return f"Item(id: {self.id}, title: {self.title}, status: {self.status}"

    
    def __hash__(self):
        return hash(self.id) + hash(self.title) * 7 + hash(self.status) * 19


    def __eq__(self, other):
        return self.id == other.id and self.title == other.title and self.status == other.status 