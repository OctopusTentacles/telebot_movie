"""
Модуль команды /remove_favorite, удаление из избранного.
"""


from database import remove_favorite_movie
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import Message


@bot.message_handler(commands=['remove_favorite'])
@logger.catch
def remove_favorite(message: Message):
    """
    Обработчик команды /remove_favorite.

    Args:
        message (Message): Объект сообщения, представляющий запрос пользователя.

    Returns:
        None
    """

    bot.set_state(message.chat.id, UserInputState.remove_favorite)
    current_state = bot.get_state(message.chat.id)
    logger.info(f'Current state: {current_state}')

    bot.send_message(
        message.chat.id,
        'Введите название фильма для удаления из избранного:'
    )