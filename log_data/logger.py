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
    compression='zip',
    level='INFO'
)

# можно обработать исключения - @logger.catch, но только исключения.
# поэтому сделаем свой декоратор для инфо и ошибок:
def log_decorator(func):
    def wrapper(message):
        try:
            result = func(message)
            logger.info(f'Function {func.__name__} run by {message.from_user.full_name}')
            return result
        except Exception as exc:
            logger.error(f'An error occurred in {func.__name__}: {exc}')
            raise
    return wrapper
