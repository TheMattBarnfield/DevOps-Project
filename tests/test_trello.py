from unittest.mock import patch, MagicMock
from trello import Trello, TrelloConfig
from status import NOT_STARTED, COMPLETED, IN_PROGRESS
from item import Item
import sys
import pytest
from api_client import ApiClient

def init_trello():
    config = TrelloConfig('key', 'token', 'url', 'board_id')
    api_client = ApiClient()
    api_client.get = mock_get([
        {
            "id": "5eeb648682bb2c685cc659f0",
            "name": NOT_STARTED,
            "closed": False,
            "pos": 1,
            "softLimit": None,
            "idBoard": "5eeb6486ebbfa66d2e519922",
            "subscribed": False
        },
        {
            "id": "5eeb648623bb2c685cc659f0",
            "name": IN_PROGRESS,
            "closed": False,
            "pos": 2,
            "softLimit": None,
            "idBoard": "5eeb6486ebbfa66d2e519922",
            "subscribed": False
        },
        {
            "id": "5eeb6486cae807625c9f0819",
            "name": COMPLETED,
            "closed": False,
            "pos": 3,
            "softLimit": None,
            "idBoard": "5eeb6486ebbfa66d2e519922",
            "subscribed": False
        }
    ])
    trello = Trello(config, api_client)
    return trello, api_client, config


def test_gets_items():
    trello, api_client, config = init_trello()
    api_client.get = mock_get([
        {
            "id": "5eeb7b0218807a823e44e373",
            "checkItemStates": None,
            "closed": False,
            "dateLastActivity": "2020-06-18T14:32:34.674Z",
            "desc": "",
            "descData": None,
            "dueReminder": None,
            "idBoard": "5eeb6486ebbfa66d2e519922",
            "idList": "5eeb648682bb2c685cc659f0",
            "idMembersVoted": [],
            "idShort": 6,
            "idAttachmentCover": None,
            "idLabels": [],
            "manualCoverAttachment": False,
            "name": "test name 1",
            "pos": 32771,
            "shortLink": "Ee8ozSAd",
            "isTemplate": False,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": False,
                "votes": 0,
                "viewingMemberVoted": False,
                "subscribed": False,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": None,
                "comments": 0,
                "attachments": 0,
                "description": False,
                "due": None,
                "dueComplete": False
            },
            "dueComplete": False,
            "due": None,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/Ee8ozSAd",
            "subscribed": False,
            "url": "https://trello.com/c/Ee8ozSAd/6-now-with-urlfor",
            "cover": {
                "idAttachment": None,
                "color": None,
                "idUploadedBackground": None,
                "size": "normal",
                "brightness": "light"
            }
        },
        {
            "id": "5eeb838b1541f3656cee5b27",
            "checkItemStates": None,
            "closed": False,
            "dateLastActivity": "2020-06-18T15:09:02.988Z",
            "desc": "",
            "descData": None,
            "dueReminder": None,
            "idBoard": "5eeb6486ebbfa66d2e519922",
            "idList": "5eeb6486cae807625c9f0819",
            "idMembersVoted": [],
            "idShort": 8,
            "idAttachmentCover": None,
            "idLabels": [],
            "manualCoverAttachment": False,
            "name": "test name 2",
            "pos": 49155,
            "shortLink": "5Nexn2os",
            "isTemplate": False,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": False,
                "votes": 0,
                "viewingMemberVoted": False,
                "subscribed": False,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": None,
                "comments": 0,
                "attachments": 0,
                "description": False,
                "due": None,
                "dueComplete": False
            },
            "dueComplete": False,
            "due": None,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/5Nexn2os",
            "subscribed": False,
            "url": "https://trello.com/c/5Nexn2os/8-now-with-parsing",
            "cover": {
                "idAttachment": None,
                "color": None,
                "idUploadedBackground": None,
                "size": "normal",
                "brightness": "light"
            }
        }
    ])

    items = trello.get_items()
    
    api_client.get.assert_called_once_with(f'{config.url}/boards/{config.board_id}/cards', config.credentials)
    
    assert set(items) == set([
        Item('5eeb7b0218807a823e44e373', 'test name 1', NOT_STARTED),
        Item('5eeb838b1541f3656cee5b27', 'test name 2', COMPLETED)
    ])

def test_get_item():
    trello, api_client, config = init_trello()
    api_client.get = mock_get({
        "id": "5eeb7b0218807a823e44e373",
        "checkItemStates": [],
        "closed": False,
        "dateLastActivity": "2020-06-18T14:32:34.674Z",
        "desc": "",
        "descData": None,
        "dueReminder": None,
        "idBoard": "5eeb6486ebbfa66d2e519922",
        "idList": "5eeb648682bb2c685cc659f0",
        "idMembersVoted": [],
        "idShort": 6,
        "idAttachmentCover": None,
        "idLabels": [],
        "manualCoverAttachment": False,
        "name": "test item",
        "pos": 32771,
        "shortLink": "Ee8ozSAd",
        "isTemplate": False,
        "dueComplete": False,
        "due": None,
        "email": None,
        "labels": [],
        "shortUrl": "https://trello.com/c/Ee8ozSAd",
        "url": "https://trello.com/c/Ee8ozSAd/6-now-with-urlfor",
        "cover": {
            "idAttachment": None,
            "color": None,
            "idUploadedBackground": None,
            "size": "normal",
            "brightness": "light"
        },
        "idMembers": [],
        "badges": {
            "attachmentsByType": {
                "trello": {
                    "board": 0,
                    "card": 0
                }
            },
            "location": False,
            "votes": 0,
            "viewingMemberVoted": False,
            "subscribed": False,
            "fogbugz": "",
            "checkItems": 0,
            "checkItemsChecked": 0,
            "checkItemsEarliestDue": None,
            "comments": 0,
            "attachments": 0,
            "description": False,
            "due": None,
            "dueComplete": False
        },
        "subscribed": False,
        "idChecklists": []
    })
    
    item = trello.get_item('5eeb7b0218807a823e44e373')
    api_client.get.assert_called_once_with(f'{config.url}/cards/5eeb7b0218807a823e44e373', config.credentials)
    assert item == Item('5eeb7b0218807a823e44e373', 'test item', NOT_STARTED)


def test_get_item_returns_none_when_not_found():
    trello, api_client, config = init_trello()
    api_client.get = mock_get({}, 404)
    item = trello.get_item('incorrect')
    api_client.get.assert_called_once_with(f'{config.url}/cards/incorrect', config.credentials)
    assert item == None


def test_set_status_throws_when_status_is_invalid():
    trello, api_client, config = init_trello()
    with pytest.raises(ValueError) as error:
        trello.set_status('id', 'invalid_status')
    assert "Attempted to set card id to have invalid status: invalid_status" == str(error.value)

def mock_get(response_body, status_code=200):
    response = MagicMock()
    response.json.return_value = response_body
    response.status_code = status_code
    return MagicMock(return_value=response)
