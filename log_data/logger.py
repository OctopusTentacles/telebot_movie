"""Модуль логирования.

param:
    rotation - размер файла bot.log.
    level - уровень логирования от INFO и выше.
"""


import os

from loguru import logger



# текущий dir:
cur_dir = os.path.dirname(__file__)

# Удаление стандартного логгера чтобы избавиться от вывода в консоль:
logger.remove()

# Настройка логирования в файл telebot_movie.log:
logger.add(
    os.path.join(cur_dir, 'telebot_movie.log'),
    rotation='10MB',
    level='INFO'
)

# можно обработать исключения - используем декоратор:
# @logger.catch
