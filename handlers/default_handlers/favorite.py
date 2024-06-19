"""
Модуль команды /add_favorite, добавление в избранное.
"""


from database import add_favorite_movie, check_user_registration
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import Message


@bot.message_handler(commands=['add_favorite'])
@logger.catch
def add_favorite(message: Message):
    """
    Обработчик команды /add_favorite.

    Args:
        message (Message): Объект сообщения, представляющий запрос пользователя.

    Returns:
        None
    """
    user_id = message.from_user.id

    # Проверка регистрации пользователя:
    if not check_user_registration(user_id):
        bot.send_message(
            message.chat.id,
            'Вы не зарегистрированы!',
            'Пожалуйста, зарегистрируйтесь с помощью /start'
        )
        return
    
    bot.set_state(message.chat.id, UserInputState.favorite)
    bot.send_message(message.chat.id, '"Введите название фильма:')





    
    # Извлечение названия фильма из сообщения пользователя
    movie_name = message.text.replace('/add_favorite', '').strip()

    if not movie_name:
        bot.send_message(
            message.chat.id,
            'Пожалуйста, укажите название фильма после команды /add_favorite.'
        )
        return
    
    if add_favorite_movie(user_id, movie_name):
        bot.send_message(
            message.chat.id,
            f'Фильм "{movie_name}" добавлен в избранное.'
        )
    else:
        bot.send_message(
            message.chat.id,
            'Что-то пошло не так... Попробуйте снова.'
        )
