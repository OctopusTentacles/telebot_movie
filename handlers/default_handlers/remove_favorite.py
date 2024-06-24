"""
Модуль команды /remove_favorite, удаление из избранного.
"""


from database import remove_favorite_name
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

@bot.message_handler(state=UserInputState.remove_favorite)
@logger.catch
def handle_remove_favorite_name(message: Message):
    """
    Обработчик ввода названия фильма для удаления из избранного.

    Args:
        message (Message): Сообщение с названием фильма от пользователя.

    Returns:
        None
    """
    movie_name = message.text
    user_id = message.from_user.id

    if remove_favorite_name(user_id, movie_name):
        bot.send_message(
            message.chat.id,
            f'Фильм "{movie_name}" удалён из избранного.'
        )
        logger.info(f'Removed favorite {movie_name}')
    else:
        bot.send_message(
            message.chat.id,
            'Фильм не найден в избранном или произошла ошибка при удалении.'
        )
    bot.delete_state(message.chat.id)
