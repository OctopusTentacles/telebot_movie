"""Модуль кнопки регистрации нового пользователя."""


from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup


def registration_button():
    """Возвращает кнопку регистрации.

    Returns:
        types.InlineKeyboardMarkup: Объект кнопки "ЗАРЕГИСТРИРОВАТЬСЯ".
    """
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='ЗАРЕГИСТРИРОВАТЬСЯ', callback_data='register')

    keyboard.add(button)

    return keyboard
