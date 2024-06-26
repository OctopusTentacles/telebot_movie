"""Модуль с настройками бота. 
В нем хранятся конфиденциальные данные, такие как токен бота.
"""


import os
import sys

from dotenv import find_dotenv
from dotenv import load_dotenv


if find_dotenv is None:
    sys.exit(
        'Переменные окружения не загружены, так как отсутствует файл .env'
    )
else:
    load_dotenv()


USERNAME = os.getenv('USERNAME')
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')

DEFAULT_COMMANDS = (
    ('start', 'перезапустить бота'),
    ('main', 'главное меню бота'),
    ('history', 'краткая история пользователя'),
    ('help', 'вывести справку'),
    ('add_favorite', 'добавить в избранное'),
    ('remove_favorite', 'удалить из избранного'),
)

# CUSTOM_COMMANDS = (
#     ('pop_movies', 'получить популярные фильмы'),
#     ('pop_serials', 'получить популярные сериалы'),
#     ('pop_cartoons', 'получить популярные мультфильмы'),
# )
