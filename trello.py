from item import Item
from status import NOT_STARTED, COMPLETED, IN_PROGRESS
from datetime import datetime

DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

class TrelloConfig:
    def __init__(self, key, token, url, board_id):
        self._credentials = {
            "key": key,
            "token": token
        }
        self._url = url
        self._board_id = board_id

    @property
    def credentials(self):
        return self._credentials

    @property
    def url(self):
        return self._url

    @property
    def board_id(self):
        return self._board_id


class Trello:
    def __init__(self, config, api_client):
        self._url = config.url
        self._credentials = config.credentials
        self._board_id = config.board_id
        self._api_client = api_client

        trelloLists = self._api_client.get(f"{self._url}/boards/{self._board_id}/lists", self._credentials).json()
        self._listIdToName = {list['id']: list['name'] for list in trelloLists}
        self._listNameToId = {list['name']: list['id'] for list in trelloLists}
        assert(set(self._listNameToId.keys()) == set([NOT_STARTED, IN_PROGRESS, COMPLETED]))



    def get_items(self):
        cards = self._api_client.get(f"{self._url}/boards/{self._board_id}/cards", self._credentials).json()
        return [self.parseTrelloCard(card) for card in cards]


    def get_item(self, id):
        response = self._api_client.get(f"{self._url}/cards/{id}", self._credentials)
        if response.status_code != 200:
            return None
        return self.parseTrelloCard(response.json())


    def add_item(self, title):
        self._api_client.post(f"{self._url}/cards", {
            "name": title,
            "idList": self._listNameToId[NOT_STARTED],
            **self._credentials
        })


    def set_status(self, id, status):
        if not status in self._listNameToId.keys():
            raise ValueError(f"Attempted to set card {id} to have invalid status: {status}")

        self._api_client.put(f"{self._url}/cards/{id}", params={
            "idList": self._listNameToId[status],
            **self._credentials
        })


    def delete_item(self, id):
        self._api_client.delete(f"{self._url}/cards/{id}", self._credentials)


    def parseTrelloCard(self, trelloCard):
        return Item(
            id=trelloCard['id'],
            title=trelloCard['name'],
            status=self._listIdToName[trelloCard['idList']],
            last_updated=datetime.strptime(trelloCard['dateLastActivity'], DATE_TIME_FORMAT)
        )

    def create_test_board(self):
        board_id = self._api_client.post(f"{self._url}/boards", params={
            "name": "todo_app_test",
            "idBoardSource": self._board_id,
            **self._credentials
        }).json()['id']

        newConfig = TrelloConfig(self._credentials['key'], self._credentials['token'], self._url, board_id)
        return Trello(newConfig, self._api_client)

        

    def delete_board(self):
        self._api_client.delete(f"{self._url}/boards/{self._board_id}", params=self._credentials)

