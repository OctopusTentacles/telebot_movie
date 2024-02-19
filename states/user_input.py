"""Модуль состояний пользователя."""


from telebot.handler_backends import State, StatesGroup


class UserInputState(StatesGroup):
    main = State()
    history = State()
    help = State()

    pop = State()
    wait = State()
    new = State()

    film = State()
    serial = State()
    cartoon = State()
