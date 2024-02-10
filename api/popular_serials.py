"""Модуль для работы с API.

Получает список популярных сериалов из новинок.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def populars():
    url = (
        f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&'
        f'selectFields=name&selectFields=year&selectFields=countries&'
        f'selectFields=genres&sortField=rating.kp&sortType=-1&'
        f'type=serial&year=2024&lists=popular-films'
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
                year = content.get('year')
                genres_data = content.get('genres', [])
                genres = ', '.join(
                    genre.get('name') for genre in genres_data
                )
                countries_data = content.get('countries', [])
                countries = ', '.join(
                    country.get('name') for country in countries_data
                )

                message_text += (
                    f'{count}.  {name}\n'
                    f'      {year}\n'
                    f'      {countries}\n'
                    f'      {genres}\n\n'
                )

    return message_text