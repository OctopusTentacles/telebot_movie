"""Модуль команды pop из кнопки ГЛАВНОГО МЕНЮ популярное."""


from api import popular_films
from keyboards.inline import type_keyboard
from loader import bot
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'pop')
def bot_popular(call: CallbackQuery):
    bot.send_message(
        call.message.chat.id, 'ПОДМЕНЮ. ВЫБЕРИ ТИП:', 
        reply_markup=type_keyboard()
    )
    text = popular_films.populars()
    bot.send_message(call.message.chat.id, 'Вот самое популярное:', text)