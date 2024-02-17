"""Модуль для работы с API.

Получает список ожидаемых премьер.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def awaits():
    url = (
        f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&'
        f'selectFields=name&selectFields=premiere&selectFields=votes&'
        f'selectFields=poster&selectFields=countries&selectFields=videos&'
        f'sortField=votes.await&sortType=-1&year=2024-2025'
    )

    if url is not None:
        headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            contents = data.get('docs')

            count = 0
            message_text = '\n'

            for content in contents:
                count += 1
                name = content.get('name')

                premiere_data = content.get('premiere', {}).get('world')
                if premiere_data:
                    premiere = premiere_data.split('T')[0]
                else:
                    premiere = 'неизвестно'
