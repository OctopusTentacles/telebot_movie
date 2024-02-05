"""Модуль для работы с API.

Получает популярный фильм на сегодня из новинок.
"""


import requests

from config_data import config
from io import BytesIO


def popular_today():
    url = (
        f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=1&'
        f'selectFields=name&sortField=rating.kp&sortType=-1&year=2024&lists=popular-films'
    )

    if url is not None:

        headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            contents = data.get('docs')