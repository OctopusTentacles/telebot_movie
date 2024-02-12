"""Модуль команды help.

Описание бота и его функционала.
"""


from loader import bot
from log_data import logger
from telebot.types import Message


@bot.message_handler(commands=['help'])
@logger.catch
def bot_help(message: Message):
    help_text = (
        'Это бот в фильмотеке,\n'
        'Как библиотекарь в библиотеке!\n\n'
        ''
        ''
    )