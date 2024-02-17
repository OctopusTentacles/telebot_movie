"""Модуль команды await из кнопки ГЛАВНОГО МЕНЮ ожидаемое."""


from api import awaits_api
from loader import bot
from log_data import logger
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=lambda call: call.data == 'await')
@logger.catch
def callback_awaits(call: CallbackQuery):
    await_info = awaits_api.awaits_api()
    bot.send_message(call.message.chat.id, 'ОЖИДАЕМЫЕ ПРЕМЬЕРЫ:', await_info)