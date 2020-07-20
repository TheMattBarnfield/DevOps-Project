import os
from trello import TrelloConfig
from dotenv import find_dotenv, load_dotenv

def loadEnv(key):
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"No value set for {key}")
    return value

class Config:
    def __init__(self, dotenv):
        file_path = find_dotenv(dotenv)
        load_dotenv(file_path, override=True)
        self.trello_config = TrelloConfig(
            loadEnv('TRELLO_KEY'),
            loadEnv('TRELLO_TOKEN'),
            loadEnv('TRELLO_URL'),
            loadEnv('TRELLO_BOARD_ID')
        )