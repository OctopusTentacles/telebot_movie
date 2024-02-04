"""Модуль основных кнопок бота. Главное меню."""


from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup


def main_keyboard():
    """Возвращает основную клавиатуру.

    Returns:
        types.InlineKeyboardMarkup: Объект основной клавиатуры.
    """
    keyboard = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='Популярное', callback_data='pop')

    keyboard.add(button_1)

    return keyboard