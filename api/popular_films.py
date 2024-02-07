"""Модуль для работы с API.

Получает список популярных фильмов из новинок.
"""


import requests

from config_data import config
from io import BytesIO


def populars():
    url = (
        ''
    )

    if url is not None:

        headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            contents = data.get('docs')

            count = 0
            message_text = ''

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
                    f'{count}. {name}\n'
                    f'  {year}\n'
                    f'  {countries}\n'
                    f'  {genres}\\n'
                )

    return message_text