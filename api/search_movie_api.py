"""Модуль для работы с API.

Получает фильм по названию, введенному пользователем.
"""


import requests

from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def search_movie_api(url):
    url = url

    headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        for content in contents:
            poster = content.get('poster', {}).get('previewUrl')
            title = content.get('name')
            year = content.get('year')

            premiere_data = content.get('premiere', {}).get('world')
            if premiere_data:
                premiere = premiere_data.split('T')[0]
            else:
                premiere = 'неизвестно'

            movieLength = content.get('movieLength')
            seriesLength = content.get('seriesLength')
            if movieLength is None and seriesLength is None:
                length = 0
            elif seriesLength is None:
                length = movieLength
            else:
                length = seriesLength

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

            genres_data = content.get('genres', [])
            genres = ', '.join(genre.get('name') for genre in genres_data)
            
            countries_data = content.get('countries',  [])
            countries = ', '.join(country.get('name') for country in countries_data)

            description = content.get('description')

            rate_kp = content.get('rating', {}).get('kp')
            rate_imdb = content.get('rating', {}).get('imdb')

            trailers_data = content.get('videos', {}).get('trailers', [])
            if trailers_data:
                trailer = trailers_data[0].get('url', '')
            else:
                trailer = 'не сняли'

        message_text_1 = (
            f'{title}   ({year})\n\n'
            f'премьера: {premiere}\n\n'
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
            f'трейлер: {trailer}'
        )

        return message_text_1, message_text_2, poster
    else:
        logger.error(
            'Failed to fetch SEARCH MOVIE data from API.'
            f'Status code: {response.status_code}'
        )
        return None, None, None




