"""Модуль команды старт."""


from loader import bot
from telebot.types import Message
from api import popular_today


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f'Привет, {message.from_user.full_name}!')

    text = popular_today.popular_today()
    bot.send_message(message, f'Посмотри\n\n{text}')