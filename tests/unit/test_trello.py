from unittest.mock import MagicMock
from status import NOT_STARTED, COMPLETED, IN_PROGRESS
from item import Item
import sys
import pytest
from datetime import datetime
from ..mock_trello import get_mock_trello, mock_get, mock_get_item, mock_get_items
from config import Config


@pytest.fixture
def trello_fixture():
    config = Config('.env.test')
    yield get_mock_trello(config.trello_config)

def test_get_items(trello_fixture):
    trello, api_client, trello_config = trello_fixture
    api_client.get = mock_get_items()

    items = trello.get_items()
    
    api_client.get.assert_called_once_with(f'{trello_config.url}/boards/{trello_config.board_id}/cards', trello_config.credentials)
    
    assert set(items) == set([
        Item('5eeb7b0218807a823e44e373', 'test name 1', NOT_STARTED, datetime(2020, 6, 18, 14, 32, 34, 674000)),
        Item('5eeb838b1541f3656cee5b27', 'test name 2', COMPLETED, datetime(2020, 6, 18, 15, 9, 2, 988000))
    ])

def test_get_item(trello_fixture):
    trello, api_client, trello_config = trello_fixture
    api_client.get = mock_get_item()
    
    item = trello.get_item('5eeb7b0218807a823e44e373')
    api_client.get.assert_called_once_with(f'{trello_config.url}/cards/5eeb7b0218807a823e44e373', trello_config.credentials)
    assert item == Item('5eeb7b0218807a823e44e373', 'test item', NOT_STARTED, datetime(2020, 6, 18, 14, 32, 34, 674000))


def test_get_item_returns_none_when_not_found(trello_fixture):
    trello, api_client, trello_config = trello_fixture
    api_client.get = mock_get({}, 404)
    item = trello.get_item('incorrect')
    api_client.get.assert_called_once_with(f'{trello_config.url}/cards/incorrect', trello_config.credentials)
    assert item == None


def test_set_status_throws_when_status_is_invalid(trello_fixture):
    trello, api_client, trello_config = trello_fixture
    with pytest.raises(ValueError) as error:
        trello.set_status('id', 'invalid_status')
    assert "Attempted to set card id to have invalid status: invalid_status" == str(error.value)


