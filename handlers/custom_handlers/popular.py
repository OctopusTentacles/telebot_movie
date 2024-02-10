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

@bot.callback_query_handler(func=lambda call: call.data == 'film')
def callback_film_handler(call: CallbackQuery):
    film_info = popular_films.populars()
    bot.send_message(call.message.chat.id, film_info)

@bot.callback_query_handler(func=lambda call: call.data == 'serial')
def callback_serial_handler(call: CallbackQuery):
    serial_info = popular_serials.populars()
    bot.send_massage(call.message.chat.id, serial_info)