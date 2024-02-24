"""Модуль для работы с API.

Получает случайный фильм.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def random_films_api():
    url = (
        'https://api.kinopoisk.dev/v1.4/movie/random?'
        'notNullFields=name&notNullFields=year&notNullFields=rating.kp&'
        'notNullFields=poster.url&notNullFields=backdrop.url&'
        'notNullFields=description&type=movie'
    )

    headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        for content in contents:
            poster = content.get('poster', {}).get('previewUrl')
            name = content.get('name')
            year = content.get('year')

            movieLength = content.get('movieLength')
            seriesLength = content.get('seriesLength')
            if seriesLength is None:
                length = movieLength
            else:
                length = seriesLength

            genres_data = content.get('genres', [])
            genres = ', '.join(genre.get('name') for genre in genres_data)

            countries_data = content.get('countries',  [])
            countries = ', '.join(
                country.get('name') for country in countries_data
            )
            
            persons_data = content.get('persons', [])
            directors = ', '.join(
                person['name'] for person in persons_data 
                if person['profession'] == 'режиссеры' and
                person['name'] is not None
            )

            actors = ', '.join(
                person['name'] for person in persons_data
                if person['profession'] == 'актеры' and
                person['name'] is not None
            )

            description = content.get('description')

            rate_kp = content.get('rating', {}).get('kp')
            rate_imdb = content.get('rating', {}).get('imdb')

        message_text_1 = (
            f'{name}   ({year})\n\n'
            f'жанр: {genres}.\n\n'
            f'страна: {countries}.\n\n'
            f'режиссер: {directors}\n\n'
            f'актеры: {actors}\n\n'
            f'длительность: {length} мин.\n\n'
            f'КП: {rate_kp}\n'
            f'IMDB: {rate_imdb}\n\n'

        )
        message_text_2 = (
            f'описание:\n{description}.\n\n'
        )

        return message_text_1, message_text_2, poster
    else:
        logger.error(
            'Failed to fetch random film data from API.'
            f'Status code: {response.status_code}'
        )
        return None, None, None
