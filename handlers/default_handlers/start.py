"""Модуль команды старт."""


from api import popular_today

from database import check_user_registration
from database import get_user_name

from keyboards.inline import main_keyboard
from keyboards.inline import regs_keyboard
from loader import bot
from log_data import logger
# from log_data import log_decorator

from telebot.types import Message


@bot.message_handler(commands=['start'])
@logger.catch
def bot_start(message: Message):

    # проверка регистрации пользователя:
    if not check_user_registration(message.from_user.id):
        # Если не зарегистрирован, отправляем сообщение с кнопкой регистрации:
        bot.send_message(
            message.chat.id,
            'Добро пожаловать!\n'
            'Для продолжения необходимо зарегистрироваться!',
            reply_markup=regs_keyboard()
        )
    else:
        bot.reply_to(message, f'Привет, {get_user_name(message.from_user.id)}!')

        bot.send_message(message.chat.id, 'СЕГОДНЯ ПОПУЛЯРНОЕ:')
        text, poster = popular_today.popular_today()
        bot.send_photo(message.chat.id, photo=poster, caption=text)

        bot.send_message(
            message.chat.id, 
            '/main - ГЛАВНОЕ МЕНЮ\n'
            '/history - Краткая история пользователя\n'
            '/add_favorite <название фильма> - Добавить фильм в избранное\n'
            '/remove_favorite - Удалить из избранного\n'
            '/help - СПРАВКА'
        )
    
