"""Модуль команды new из кнопки ГЛАВНОГО МЕНЮ Новинки."""


from api import new_films_api
from api import new_serials_api
from api import new_cartoons_api

from keyboards.inline import type_keyboard
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'new')
def bot_new_content(call: CallbackQuery):
    bot.set_state(call.message.chat.id, state = UserInputState.new)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f"Current state: {current_state}")

    bot.send_message(
        call.message.chat.id, 'НОВИНКИ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )


@bot.callback_query_handler(
    state = UserInputState.new,
    func=lambda call: call.data == 'film'
)
def callback_new_film(call: CallbackQuery):
    film_info = new_films_api.new_films_api()
    bot.send_message(call.message.chat.id, film_info)
    bot.send_message(
        call.message.chat.id, 'НОВИНКИ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )


@bot.callback_query_handler(
    state = UserInputState.new,
    func=lambda call: call.data == 'serial'
)
def callback_new_serial(call: CallbackQuery):
    serial_info = new_serials_api.new_serials_api()
    bot.send_message(call.message.chat.id, serial_info)
    bot.send_message(
        call.message.chat.id, 'НОВИНКИ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )


@bot.callback_query_handler(
    state = UserInputState.new,
    func=lambda call: call.data == 'cartoon'
)
def callback_new_cartoon(call: CallbackQuery):
    cartoon_info = new_cartoons_api.new_cartoons_api()
    bot.send_message(call.message.chat.id, cartoon_info)
    bot.send_message(
        call.message.chat.id, 'НОВИНКИ: ВЫБЕРИ ТИП:',
        reply_markup=type_keyboard()
    )
