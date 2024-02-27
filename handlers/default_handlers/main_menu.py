"""Модуль команды main."""


from keyboards.inline import main_keyboard
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import Message


@bot.message_handler(commands=['main'])
@logger.catch
def bot_main(message: Message):
    bot.set_state(message.chat.id, state = UserInputState.main)

    current_state = bot.get_state(message.chat.id)
    logger.info(f"Current state: {current_state}")

    bot.reply_to(message, 'ГЛАВНОЕ МЕНЮ:', reply_markup=main_keyboard())
    