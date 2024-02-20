"""Модуль команды pop из кнопки ГЛАВНОГО МЕНЮ популярное."""


from api import popular_films
from api import popular_serials
from api import popular_cartoons
from keyboards.inline import type_keyboard
from loader import bot
from states.user_input import UserInputState
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'pop')
def bot_popular(call: CallbackQuery):
    bot.set_state(call.message.chat.id, UserInputState.pop)
    bot.send_message(
        call.message.chat.id, 'ПОПУЛЯРНОЕ: ВЫБЕРИ ТИП:', 
        reply_markup=type_keyboard()
    )




@bot.callback_query_handler(
    func=lambda call: call.data == 'film' and
    bot.get_state(call.message.chat.id) == UserInputState.pop
)
def callback_film_handler(call: CallbackQuery):
    film_info = popular_films.populars()
    bot.send_message(call.message.chat.id, film_info)
    bot.send_message(
        call.message.chat.id, 'ПОПУЛЯРНОЕ: ВЫБЕРИ ТИП:', 
        reply_markup=type_keyboard()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'serial')
def callback_serial_handler(call: CallbackQuery):
    serial_info = popular_serials.populars()
    bot.send_message(call.message.chat.id, serial_info)
    bot.send_message(
        call.message.chat.id, 'ПОПУЛЯРНОЕ: ВЫБЕРИ ТИП:', 
        reply_markup=type_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data == 'cartoon')
def callback_cartoon_handler(call: CallbackQuery):
    cartoon_info = popular_cartoons.populars()
    bot.send_message(call.message.chat.id, cartoon_info)
    bot.send_message(
        call.message.chat.id, 'ПОПУЛЯРНОЕ: ВЫБЕРИ ТИП:', 
        reply_markup=type_keyboard()
    )
