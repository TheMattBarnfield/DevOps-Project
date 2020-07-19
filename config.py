import os
from trello import TrelloConfig

def loadEnv(key):
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"No value set for {key}")
    return value

TRELLO_CONFIG = TrelloConfig(
    loadEnv('TRELLO_KEY'),
    loadEnv('TRELLO_TOKEN'),
    "https://api.trello.com/1",
    "OgyYJWzO"
)