"""Модуль для работы с API.

Получает список новинок - сериалы.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def new_serials_api():
    url = (
        'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=7&'
        'selectFields=name&selectFields=premiere&selectFields=poster&'
        'selectFields=rating&notNullFields=name&notNullFields=premiere.world&'
        'notNullFields=poster.url&notNullFields=rating.kp&'
        'sortField=premiere.world&sortType=-1&type=tv-series&year=2024&'
        'rating.kp=1-10'
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
                premiere = content.get('premiere', {}).get('world')
                premiere = premiere.split('T')[0]
                rating = content.get('rating', {}).get('kp')

                message_text += (
                    f'{count}.  {name}\n'
                    f'      премьера: {premiere}\n'
                    f'      КП: {rating}\n\n'
                )

    return message_text
