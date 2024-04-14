"""Модуль кнопки ЗАРЕГИСТРИРОВАТЬСЯ."""


from database import save_user_registration
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'register')
def register_user(call: CallbackQuery):
    bot.set_state(call.message.chat.id, UserInputState.register)
    
    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    user_id = call.from_user.id
    user_name = call.from_user.full_name
    if save_user_registration(user_id, user_name):
        logger.info()
        bot.send_message(
            call.message.chat.id,
            'Вы успешно зарегистрированы!'
        )
    else:
        bot.send_message(
            call.message.chat.id,
            'Что-то пошло не так...Начни сначала '
        )
