import os
from dotenv import find_dotenv, load_dotenv
from db_client import DbConfig


def load_env(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"No value set for {key}")
    return value


class Config:
    def __init__(self, dotenv):
        file_path = find_dotenv(dotenv)
        load_dotenv(file_path, override=True)
        self.db_config = DbConfig(
            load_env('DB_NAME'),
            load_env('DB_USER'),
            load_env('DB_PASS'),
        )
