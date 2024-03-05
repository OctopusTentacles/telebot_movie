"""Модуль для работы с API.

Из названия пользователя ищет информацию - ID,
Возвращает URL с ID - это дает полную информацию.
"""


import requests

from config_data import config
from log_data import logger
from typing import Union


@logger.catch
def create_url_name_api(encoding_title: Union[str, bytes]) -> str:
    """
    Формирует URL API для поиска информации по запросу пользователя.

    Args:
        encoding_title (str, bytes): Закодированное имя.

    Returns:
        str: URL API для получения полной информации.
    """
    url = (
        'https://api.kinopoisk.dev/v1.4/person/search?page=1&limit=1&'
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

        url = f'https://api.kinopoisk.dev/v1.4/person/{id}'

    return url
