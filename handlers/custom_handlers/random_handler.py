"""Модуль команды rand из кнопки ГЛАВНОГО МЕНЮ Рандом."""


from api import random_films_api
# from api import random_serials_api
# from api import random_cartoons_api

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
