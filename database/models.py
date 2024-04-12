"""Модуль для работы с базой данных."""


import os

from datetime import datetime
from peewee import *


# текущий dir:
cur_dir = os.path.dirname(__file__)

# Инициализация файла базы данных (SQLite) в текущем dir:
db = SqliteDatabase(os.path.join(cur_dir, 'user_history.db'))


class UserRegistration(Model):
    user_id = IntegerField(unique=True)
    username = CharField()
    favorite_movies = TextField(default='')
    registration_date = DateTimeField(default=datetime.now)




class UserRequest(Model):
    """Модель для запросов пользователя.

    Attributes:
        user_name (CharField): Имя пользователя.
        user_id (CharField): Идентификатор пользователя.
        category (CharField): Категория запроса.
        timestamp (DateTimeField): Временная метка запроса - текущее время.
    """
    user_name = CharField()
    user_id = CharField()
    category = CharField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta(type):
        """Метакласс для указания базы данных.

        Attributes:
            database = db указывает, что объект базы данных db,
            созданный с использованием SqliteDatabase, будет
            использоваться для хранения данных модели UserRequest.
        """
        database = db


# инициализация таблицы в базе данных:
db.connect()
db.create_tables(UserRegistration)
db.create_tables(UserRequest)
db.close()
