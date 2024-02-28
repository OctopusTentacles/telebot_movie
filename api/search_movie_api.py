"""Модуль для работы с API.

Ищет фильм по названию.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def search_movie_api(encoding_title):
    url = (
        'https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=1&'
        f'query={encoding_title}'
    )

    headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = data.get('docs')
        # получили краткую информацию о фильме,
        # но мы хотим полную информацию - поэтому,
        # берем ID, формируем ссылку по ID - это даст полную информацию.
        for content in contents:
            id = content.get('id')
            
        url = f'https://api.kinopoisk.dev/v1.4/movie/{id}'
