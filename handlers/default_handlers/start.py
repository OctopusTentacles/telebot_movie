"""Модуль команды старт."""


from api import popular_today
from keyboards.inline import main_keyboard
from loader import bot
from log_data import logger
# from log_data import log_decorator

from telebot.types import Message


@bot.message_handler(commands=['start'])
@logger.catch
# @log_decorator
def bot_start(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!')

    # logger.info(
    #     f'user {message.from_user.full_name} запустил бота!'
    # )

    bot.send_message(message.chat.id, 'СЕГОДНЯ ПОПУЛЯРНОЕ:')
    text, poster = popular_today.popular_today()
    bot.send_photo(message.chat.id, photo=poster, caption=text)

    bot.send_message(
        message.chat.id, 'три команды ', {'/main'}
    )
    

@bot.message_handler(commands=['main'])
@logger.catch
def bot_main(message: Message):
    bot.reply_to(message, 'ГЛАВНОЕ МЕНЮ:', reply_markup=main_keyboard())