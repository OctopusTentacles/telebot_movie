"""Модуль команды rand из кнопки ГЛАВНОГО МЕНЮ Рандом."""


import base64
import requests

from api import random_films_api
# from api import random_serials_api
# from api import random_cartoons_api

from io import BytesIO
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

@bot.callback_query_handler(
    state = UserInputState.rand,
    func=lambda call: call.data == 'film'
)
def callback_rand_film(call: CallbackQuery):
    text1, text2, poster = random_films_api.random_films_api()

    if poster:
        logger.info(f"Poster URL: {poster}")  # Добавьте эту строку для проверки URL постера
   
        # декодирование постера:
        # poster_bytes = base64.b64decode(poster)
        # poster_io = BytesIO(poster_bytes)

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
            logger.error(f"Failed to send photo: {response.status_code}, {response.text}")


        bot.send_message(call.message.chat.id, text2[:4096])
        if len(text2) > 4096:
            bot.send_message(call.message.chat.id, text2[4096:])

    bot.send_message(
        call.message.chat.id, 'РАНДОМ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )
