import os

def loadEnv(key):
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"No value set for {key}")
    return value

TRELLO_KEY = loadEnv('TRELLO_KEY')
TRELLO_TOKEN = loadEnv('TRELLO_TOKEN')
TRELLO_URL = "https://api.trello.com/1"
TRELLO_BOARD = "OgyYJWzO"
