import os

def pytest_configure():
    os.environ['TRELLO_KEY'] = "TEST"
    os.environ['TRELLO_TOKEN'] = "TEST"