"""Модуль команды старт."""


from api import popular_today
from keyboards.inline import main_keyboard
from loader import bot
from log_data import logger
# from log_data import log_decorator

from telebot.types import Message


@bot.message_handler(commands=['start'])
@logger.catch
def bot_start(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!')

    bot.send_message(message.chat.id, 'СЕГОДНЯ ПОПУЛЯРНОЕ:')
    text, poster = popular_today.popular_today()
    bot.send_photo(message.chat.id, photo=poster, caption=text)

    bot.send_message(
        message.chat.id, 
        '/main - ГЛАВНОЕ МЕНЮ\n'
        '/history - Краткая история пользователя\n'
        '/help - СПРАВКА'
    )
    
