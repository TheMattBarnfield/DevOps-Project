import app
from ..mock_trello import get_mock_trello, mock_get_items
import pytest
from config import Config

@pytest.fixture
def client_fixture():
    config = Config('.env.test')
    trello, api_client, trello_config = get_mock_trello(config.trello_config)
    test_app = app.create_app({}, trello)
    with test_app.test_client() as client:
        yield client, api_client

def test_index_page(client_fixture):
    client, api_client = client_fixture
    api_client.get = mock_get_items()
    response = client.get('/')
    assert b"test name 1" in response.data
    assert b"test name 2" in response.data
    