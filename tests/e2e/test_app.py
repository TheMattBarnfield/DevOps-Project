import os
import pytest
from threading import Thread
import app
from trello import Trello
from config import Config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from api_client import ApiClient
import time

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        yield driver

@pytest.fixture(scope='module')
def test_app():
    trello_config = Config(".env").trello_config
    trello = Trello(trello_config, ApiClient()).create_test_board()
    application = app.create_app({}, trello)

    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()

    # I really feel like this shouldn't be necessary, but otherwise selenium makes requests before flask has started
    time.sleep(1)

    yield app

    thread.join(1)
    trello.delete_board()


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'Ti-Di Ipp'