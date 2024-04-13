"""Модуль кнопки ЗАРЕГИСТРИРОВАТЬСЯ."""


from database import save_user_registration
from loader import TeleBot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'register')
def register_user(call: CallbackQuery):
    user_id = call.from_user.id
    user_name = call.from_user.full_name
    if save_user_registration(user_id, user_name):
        bot.send_message(
            call.message.chat.id,
            'Вы успешно зарегистрированы!'
        )