from requests import get, post, put, delete
from config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN, TRELLO_BOARD

CREDS = {
    "key": TRELLO_KEY,
    "token": TRELLO_TOKEN
}

trelloLists = get(f"{TRELLO_URL}/boards/{TRELLO_BOARD}/lists", params=CREDS).json()
listIdToName = {list['id']: list['name'] for list in trelloLists}
listNameToId = {list['name']: list['id'] for list in trelloLists}

def get_items():
    cards = get(f"{TRELLO_URL}/boards/{TRELLO_BOARD}/cards", params=CREDS).json()
    return [parseTrelloCard(card) for card in cards]


def get_item(id):
    reponse = get(f"{TRELLO_URL}/cards/{id}", params=CREDS)
    if response.status_code != 200:
        return None
    return parseTrelloCard(response.json())


def add_item(title):
    post(f"{TRELLO_URL}/cards", params={
        "name": title,
        "idList": listNameToId['Not Started'],
        **CREDS
    })


def set_status(id, status):
    if not status in listNameToId.keys():
        raise ValueError(f"Attempted to set card {id} to have invalid status: {status}")

    put(f"{TRELLO_URL}/cards/{id}", params={
        "idList": listNameToId[status],
        **CREDS
    })

def delete_item(id):
    delete(f"{TRELLO_URL}/cards/{id}", params=CREDS)


def parseTrelloCard(trelloCard):
    return {
        "id": trelloCard['id'],
        "status": listIdToName[trelloCard['idList']],
        "title": trelloCard['name']
    }
