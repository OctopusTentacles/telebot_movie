"""Модуль команды movie из кнопки ГЛАВНОГО МЕНЮ - Поиск фильма."""


from api import create_url_api

from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery
from urllib.parse import quote


@bot.callback_query_handler(func=lambda call: call.data == 'movie')
def user_input_title(call: CallbackQuery):
    bot.set_state(call.message.chat.id, state = UserInputState.search_movie)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    bot.send_message(call.message.chat.id, 'Введи название фильма:')


@bot.callback_query_handler(func=lambda call: call.data == 'person')
def user_input_name(call: CallbackQuery):
    bot.set_state()

# Получить введенное пользователем название и закодировать:
def encoding_title(message):
    user_title = message.text.strip()
    print(user_title)

    encoding_title = quote(user_title)
    print(encoding_title)

    url = create_url_api.create_url_api(encoding_title)
    print(url)
