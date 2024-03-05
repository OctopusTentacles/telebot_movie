"""Модуль поиска кнопки ГЛАВНОГО МЕНЮ - Поиск фильма и Поиск Актера.
"""


import requests

from api import create_url_movie_api
from api import create_url_name_api
from api import search_movie_api
from api import search_person_api

from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery
from urllib.parse import quote


# Получить введенное пользователем название и закодировать:
def encoding_title(message):

    user_input = message.text.strip()
    encoding_input = quote(user_input)

    return create_url_movie_api.create_url_movie_api(encoding_input)


# Получить введенное пользователем имя и закодировать:
def encoding_name(message):

    user_input = message.text.strip()
    encoding_input = quote(user_input)

    return create_url_name_api.create_url_name_api(encoding_input)



# ==========================================================================
@bot.callback_query_handler(func=lambda call: call.data == 'movie')
def user_input_title(call: CallbackQuery):
    bot.set_state(call.message.chat.id, state = UserInputState.search_movie)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    bot.send_message(call.message.chat.id, 'Введи название фильма:')
    bot.register_next_step_handler(call.message, callback_search_movie)


@bot.callback_query_handler(func=lambda call: call.data == 'person')
def user_input_name(call: CallbackQuery):
    bot.set_state(call.message.chat.id, state = UserInputState.search_name)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    bot.send_message(call.message.chat.id, 'Введи имя:')
    bot.register_next_step_handler(call.message, callback_search_person)


# ==========================================================================
def callback_search_movie(message):
    url = encoding_title(message)

    text_1, text_2, poster = search_movie_api.search_movie_api(url)

    response = requests.post(
        f"https://api.telegram.org/bot{bot.token}/sendPhoto",
        data={
            "chat_id": message.chat.id,
            "photo": poster,
            "caption": text_1
        }
    )
    # Обработка ответа от сервера Telegram
    if response.status_code != 200:
        logger.error(
            f"Failed to send photo: {response.status_code}, {response.text}"
        )
    # отправляем описание,
    # может превышать макс размер 4096.
    bot.send_message(message.chat.id, text_2[:4096])
    if len(text_2) > 4096:
        bot.send_message(message.chat.id, text_2[4096:])


# ==========================================================================
def callback_search_person(message):

    url = encoding_name(message)

    text_1, text_2, poster = search_person_api.search_person_api(url)

    response = requests.post(
        f"https://api.telegram.org/bot{bot.token}/sendPhoto",
        data={
            "chat_id": message.chat.id,
            "photo": poster,
            "caption": text_1
        }
    )
    # Обработка ответа от сервера Telegram
    if response.status_code != 200:
        logger.error(
            f"Failed to send photo: {response.status_code}, {response.text}"
        )
    # отправляем описание,
    # может превышать макс размер 4096.
    bot.send_message(message.chat.id, text_2[:4096])
    if len(text_2) > 4096:
        bot.send_message(message.chat.id, text_2[4096:])
