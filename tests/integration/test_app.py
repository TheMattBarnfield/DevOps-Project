import app
import pytest
from config import Config

@pytest.fixture
def client_fixture():
    test_app = app.create_app({}, use_real_db=False)
    with test_app.test_client() as client:
        yield client

def test_index_page(client_fixture):
    client = client_fixture
    response = client.get('/')
    assert b"test name 1" in response.data
    assert b"test name 2" in response.data
