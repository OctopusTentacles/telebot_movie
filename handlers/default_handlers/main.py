"""Модуль команды main."""


from api import popular_today
from keyboards.inline import main_keyboard
from loader import bot
from log_data import logger
# from log_data import log_decorator

from telebot.types import Message





@bot.message_handler(commands=['main'])
@logger.catch
def bot_main(message: Message):
    bot.reply_to(message, 'ГЛАВНОЕ МЕНЮ:', reply_markup=main_keyboard())