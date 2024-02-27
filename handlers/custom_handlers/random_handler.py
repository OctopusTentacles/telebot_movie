"""Модуль команды rand из кнопки ГЛАВНОГО МЕНЮ Рандом."""


import requests

from api import random_films_api
from api import random_serial_api
from api import random_cartoons_api

from keyboards.inline import type_keyboard
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'rand')
def bot_rand_content(call: CallbackQuery):
    bot.set_state(call.message.chat.id, state = UserInputState.rand)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    bot.send_message(
        call.message.chat.id, 'РАНДОМ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )

# ====================================================================
@bot.callback_query_handler(
    state = UserInputState.rand,
    func=lambda call: call.data == 'film'
)
def callback_rand_film(call: CallbackQuery):
    text1, text2, poster = random_films_api.random_films_api()

    # отправляем постер с подписью в чат,
    # постер содержит URL так как иначе значение не передавалось,
    # говорил что слишком большой объем данных.
    response = requests.post(
        f"https://api.telegram.org/bot{bot.token}/sendPhoto",
        data={
            "chat_id": call.message.chat.id,
            "photo": poster,
            "caption": text1
        }
    )
    # Обработка ответа от сервера Telegram
    if response.status_code != 200:
        logger.error(
            f"Failed to send photo: {response.status_code}, {response.text}"
        )
    # отправляем описание,
    # может превышать макс размер 4096.
    bot.send_message(call.message.chat.id, text2[:4096])
    if len(text2) > 4096:
        bot.send_message(call.message.chat.id, text2[4096:])

    bot.send_message(
        call.message.chat.id, 'РАНДОМ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )

# ====================================================================
@bot.callback_query_handler(
    state = UserInputState.rand,
    func=lambda call: call.data == 'serial'
)
def callback_rand_film(call: CallbackQuery):
    text1, text2, poster = random_serial_api.random_serial_api()

    # отправляем постер с подписью в чат,
    # постер содержит URL так как иначе значение не передавалось,
    # говорил что слишком большой объем данных.
    response = requests.post(
        f"https://api.telegram.org/bot{bot.token}/sendPhoto",
        data={
            "chat_id": call.message.chat.id,
            "photo": poster,
            "caption": text1
        }
    )
    # Обработка ответа от сервера Telegram
    if response.status_code != 200:
        logger.error(
            f"Failed to send photo: {response.status_code}, {response.text}"
        )
    # отправляем описание,
    # может превышать макс размер 4096.
    bot.send_message(call.message.chat.id, text2[:4096])
    if len(text2) > 4096:
        bot.send_message(call.message.chat.id, text2[4096:])

    bot.send_message(
        call.message.chat.id, 'РАНДОМ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )

# ====================================================================
@bot.callback_query_handler(
    state = UserInputState.rand,
    func=lambda call: call.data == 'cartoon'
)
def callback_rand_film(call: CallbackQuery):
    text1, text2, poster = random_cartoons_api.random_cartoons_api()

    # отправляем постер с подписью в чат,
    # постер содержит URL так как иначе значение не передавалось,
    # говорил что слишком большой объем данных.
    response = requests.post(
        f"https://api.telegram.org/bot{bot.token}/sendPhoto",
        data={
            "chat_id": call.message.chat.id,
            "photo": poster,
            "caption": text1
        }
    )
    # Обработка ответа от сервера Telegram
    if response.status_code != 200:
        logger.error(
            f"Failed to send photo: {response.status_code}, {response.text}"
        )
    # отправляем описание,
    # может превышать макс размер 4096.
    bot.send_message(call.message.chat.id, text2[:4096])
    if len(text2) > 4096:
        bot.send_message(call.message.chat.id, text2[4096:])

    bot.send_message(
        call.message.chat.id, 'РАНДОМ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )
