"""Модуль команды старт."""


from loader import bot
from telebot.types import Message
from api import popular_today


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!')

    bot.send_message(message.chat.id, 'СЕГОДНЯ ПОПУЛЯРНОЕ')
    text, poster = popular_today.popular_today()
    bot.send_photo(message.chat.id, poster, caption=text)
