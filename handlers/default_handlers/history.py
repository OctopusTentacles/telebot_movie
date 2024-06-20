""" Модуль команды history. """


from database import get_user_history
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import Message


@bot.message_handler(commands=['history'])
@logger.catch
def user_history(message: Message):
    """
    Обработчик команды /history.

    Эта функция вызывается при вводе пользователем команды /history.
    Она получает историю пользователя из базы данных 
    и отправляет её в чат.

    Args:
        message (Message): Сообщение с командой от пользователя.

    Returns:
        None
    """
    bot.set_state(message.chat.id, UserInputState.history)
    current_state = bot.get_state(message.chat.id)
    logger.info(f"Current state: {current_state}")


    user_id = message.from_user.id
    history = get_user_history(user_id)
    bot.send_message(message.chat.id, history)
    