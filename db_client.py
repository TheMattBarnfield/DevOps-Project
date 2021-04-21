import pymongo
from item import Item
from status import NOT_STARTED
from datetime import datetime
from bson.objectid import ObjectId
from dataclasses import dataclass

DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


@dataclass
class DbConfig:
    db_name: str
    db_user: str
    db_pass: str


class DbClient:
    def __init__(self, db_config: DbConfig, overwrite_db_name=False):
        db_name = "test" if overwrite_db_name else db_config.db_name
        client = pymongo.MongoClient(
            f"mongodb+srv://{db_config.db_user}:{db_config.db_pass}@cluster0.bgo8m.mongodb.net/{db_name}?retryWrites=true&w=majority"
        )
        self.items = client[db_name].items

    def add_item(self, title: str):
        self.items.insert_one({
            "title": title,
            "status": NOT_STARTED,
            "last_updated": datetime.now().strftime(DATE_TIME_FORMAT)
        })

    def get_items(self) -> [Item]:
        db_items = self.items.find()
        return [self.parse_item_from_db(item) for item in db_items]

    def set_status(self, id: str, status: str):
        query = {
            "_id": ObjectId(id)
        }
        update = {
            "$set": {
                "status": status,
                "last_updated": datetime.now().strftime(DATE_TIME_FORMAT)
            }
        }
        self.items.update_one(query, update)

    def delete_item(self, id: str):
        self.items.delete_one({"_id": ObjectId(id)})

    def parse_item_from_db(self, db_item) -> Item:
        return Item(
            id=str(db_item['_id']),
            title=db_item['title'],
            status=db_item['status'],
            last_updated=datetime.strptime(db_item['last_updated'], DATE_TIME_FORMAT)
        )


class MockDbClient:
    def __init__(self):
        self.db = {}
        self.next_id = 0
        self.add_item("test name 1")
        self.add_item("test name 2")

    def add_item(self, title: str):
        self.db[self.next_id] = Item(self.next_id, title, NOT_STARTED, datetime.now())
        self.next_id += 1

    def get_items(self) -> [Item]:
        return self.db.values()

    def set_status(self, id: str, status: str):
        self.db[id].status = status
        self.db[id].last_updated = datetime.now()

    def delete_item(self, id: str):
        del self.db[id]
