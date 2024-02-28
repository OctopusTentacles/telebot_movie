"""Модуль для работы с API.

Ищет фильм по названию.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def search_movie_api():
    