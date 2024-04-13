"""Модуль для работы с базой данных."""


import os

from datetime import datetime
from peewee import *


# текущий dir:
cur_dir = os.path.dirname(__file__)

# Инициализация файла базы данных (SQLite) в текущем dir:
db = SqliteDatabase(os.path.join(cur_dir, 'user_history.db'))


class UserRegistration(Model):
    """Модель для хранения зарегистрированных пользователях.

    Args:
        user_id (IntegerField): Идентификатор пользователя.    
        user_name (CharField): Имя пользователя.
        favorite_movies (TextField): список избранного.
        registration_date (DateTimeField): Временная метка запроса - текущее время.
    """
    user_id = IntegerField(unique=True)
    username = CharField()
    favorite_movies = TextField(default='')
    registration_date = DateTimeField(default=datetime.now)

    class Meta:
        database = db


class UserRequest(Model):
    """Модель для запросов пользователя.

    Attributes:
        user_name (CharField): Имя пользователя.
        user_id (IntegerField): Идентификатор пользователя.
        category (CharField): Категория запроса.
        timestamp (DateTimeField): Временная метка запроса - текущее время.
    """
    user_name = CharField()
    user_id = IntegerField()
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
db.create_tables([UserRegistration, UserRequest])
db.close()
