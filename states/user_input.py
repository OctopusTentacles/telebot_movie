"""Модуль состояний пользователя."""


from telebot.handler_backends import State, StatesGroup


class UserInputState(StatesGroup):
    main = State()
    history = State()
    help = State()

    pop = State()
    wait = State()
    new = State()
    rand = State()
    search_movie = State()
    search_name = State()
    register = State()

    film = State()
    serial = State()
    cartoon = State()
