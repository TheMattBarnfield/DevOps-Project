import os
import pytest
from threading import Thread
import app
from trello import Trello
from config import Config
from selenium import webdriver
from api_client import ApiClient
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver

# @pytest.fixture(scope='module')
# def test_app():
#     trello_config = Config(".env").trello_config
#     trello = Trello(trello_config, ApiClient()).create_test_board()
#     application = app.create_app({}, trello)
#
#     thread = Thread(target=lambda: application.run(use_reloader=False))
#     thread.daemon = True
#     thread.start()
#
#     # I really feel like this shouldn't be necessary, but otherwise selenium makes requests before flask has started
#     time.sleep(1)
#
#     yield app
#
#     thread.join(1)
#     trello.delete_board()
#
#
# def test_task_journey(driver, test_app):
#     driver.implicitly_wait(10)
#     driver.get('http://localhost:5000/')
#
#     assert driver.title == 'Ti-Di Ipp'
#
#     new_item_title = driver.find_element(By.ID, 'title')
#     new_item_title.send_keys('Test task')
#     new_item_title.send_keys(Keys.RETURN)
#
#     item = driver.find_element(By.CLASS_NAME, 'not-started')
#     assert 'Test task' in item.text
#
#     start_button = item.find_element(By.CLASS_NAME, 'start')
#     start_button.click()
#
#     item = driver.find_element(By.CLASS_NAME, 'in-progress')
#     assert 'Test task' in item.text
#
#     complete_button = item.find_element(By.CLASS_NAME, 'mark-completed')
#     complete_button.click()
#
#     item = driver.find_element(By.CLASS_NAME, 'completed')
#     assert 'Test task' in item.text
#
#     delete_button = item.find_element(By.CLASS_NAME, 'delete')
#     delete_button.click()
#
#     assert 'Test task' not in driver.page_source
