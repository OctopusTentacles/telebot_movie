"""Модуль команды pop из кнопки ГЛАВНОГО МЕНЮ популярное."""


from api import
from keyboards.inline import
from loader import bot
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'pop')
def bot_popular(call: CallbackQuery):
    bot.send_message(call.message.chat.id, 'Вот самое популярное:')