"""Модуль для работы с API.

Получает популярный фильм на сегодня из новинок.
"""


import requests

from config_data import config
from io import BytesIO


def popular_today():
    url = (
        f'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=1&'
        f'selectFields=name&selectFields=rating&selectFields=movieLength&'
        f'selectFields=genres&selectFields=countries&selectFields=poster&'
        f'selectFields=premiere&sortField=rating.kp&sortType=-1&'
        f'year=2024&lists=popular-films'
    )

    if url is not None:

        headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            contents = data.get('docs')

            for content in contents:
                poster = content.get('poster', {}).get('previewUrl')
                name = content.get('name')
                rating = content.get('rating', {}).get('kp')
                movieLength = content.get('movieLength')

                genres_data = content.get('genres', [])
                genres = ', '.join(genre.get('name') for genre in genres_data)

                countries_data = content.get('countries', [])
                countries = ', '.join(country.get('name') for country in countries_data)

                premiere_data = content.get('premiere', {}).get('world')
                if premiere_data:
                    premiere = premiere_data.split('T')[0]
                else:
                    premiere = 'неизвестно'

                message_text = (
                    f'{name}\n\n'
                    f'длительность: {movieLength} мин.\n\n'

                    f'премьера: {premiere}\n\n'
                    f'жанр: {genres}.\n\n'
                    f'страна: {countries}.\n\n'
                    f'КП: {rating}\n'
                )

                if poster:
                    image_io = BytesIO(requests.get(poster).content)
                    # положить в кэш по id - message_text и poster:
    
    return message_text, image_io
