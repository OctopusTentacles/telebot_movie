"""Модуль для работы с API.

Получает актера/режиссера по имени, введенному пользователем.
"""


import html
import re
import requests


from config_data import config
from io import BytesIO
from log_data import logger


def remove_html(text: str) -> str:
    """В фактах встречаются ссылки типа -
    <a href="/name/77564/" class="all">Дженнифер Сайм</a> 
    И HTML-коды  - попробуем их обработать.

    html.unescape:
        преобразует HTML-коды в соответствующие символы.

    pattern:
        <(.*?)> - любое вхождение любых символов между < >.

    re.sub:
        удаляем паттерн из текста.
    """
    text = html.unescape(text)
    pattern = re.compile(r'<(.*?)>')
    text = re.sub(pattern, '', text)

    return text


@logger.catch
def search_person_api(url):

    headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]

        for content in contents:
            poster = content.get('photo')
            title = content.get('name')
            age = content.get('age')
            growth = content.get('growth')
            countAwards = content.get('countAwards')

            birthday_data = content.get('birthday')
            if birthday_data:
                birthday = birthday_data.split('T')[0]
            else:
                birthday = 'неизвестно'

            birthPlace_data = content.get('birthPlace', [])
            if birthPlace_data:
                birthPlace = ', '.join(
                    place['value'] for place in birthPlace_data
                    if place['value'] is not None
                )
            else:
                birthPlace = 'неизвестно'

            profession_data = content.get('profession', [])
            profession = ', '.join(
                profi['value'] for profi in profession_data
                if profi['value'] is not None
            )

            facts_data = content.get('facts', [])
            if facts_data:
                facts = '\n\n'.join(
                    remove_html(fact['value']) for fact in facts_data
                    if fact['value'] is not None
                )
            else:
                facts = 'ФАКТЫ - неизвестно'

            message_text_1 = (
                f'{title}   ({age})\n\n'
                f'дата рождения: {birthday}\n\n'
                f'место раждения: {birthPlace}\n\n'
                f'рост: {growth}\n\n'
                f'профессия: {profession}\n\n'
                f'количество наград: {countAwards}'
            )
            message_text_2 = (
                f'{facts}'
            )

        return message_text_1, message_text_2, poster
    else:
        logger.error(
            'Failed to fetch SEARCH PERSON data from API.'
            f'Status code: {response.status_code}'
        )
        return None, None, None
