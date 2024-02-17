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
        'Список доступных команд:\n'
        '/start - Запустить бота\n'
        '/main - Показать главное меню\n'
        '/history - Краткая история пользователя\n'
        '/help - Вывести это сообщение\n\n'
        'Взаимодействие с ботом осуществляется через эти команды '
        'и кнопки бота, которые будут доступны в ответах.'
    )

    bot.reply_to(message, help_text)
    