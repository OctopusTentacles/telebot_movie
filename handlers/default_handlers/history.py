""" Модуль команды history. """


from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import Message


@bot.message_handler(commands=['history'])
@logger.catch
def user_history(message: Message):
    """_summary_

    Args:
        message (Message): _description_
    """