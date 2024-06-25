"""Модуль команды favorite из кнопки ГЛАВНОГО МЕНЮ Избранное."""


from database import get_favorite_movie
from keyboards.inline import type_keyboard
from loader import bot
from log_data import logger
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'favorite')
def show_favorite_movies(call: CallbackQuery):
    """
    Обработчик нажатия кнопки "Избранное".

    Args:
        call (CallbackQuery): Объект, 
        представляющий вызов обратного запроса от пользователя.

    Returns:
        None
    """
    bot.set_state(call.message.chat.id, state = UserInputState.favorite)

    current_state = bot.get_state(call.message.chat.id)
    logger.info(f'Current state: {current_state}')

    user_id = call.from_user.id
    # Получение списка избранных фильмов
    favorite_movies = get_favorite_movie(user_id)

    if favorite_movies:
        movie_list = '\n'.join(f'{movie}'for movie in favorite_movies)
        bot.send_message(
            call.message.chat.id,
            f'⭐ Ваши избранные фильмы:\n\n{movie_list}'
        )    
    else:
        bot.send_message(
            call.message.chat.id,
            'Ваш список избранных фильмов пуст.'
        )
