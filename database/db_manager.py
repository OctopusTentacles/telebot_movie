""" Модуль взаимодействия с базой данных. """

import json

from datetime import datetime
from log_data import logger
from .models import UserRegistration


def check_user_registration(user_id: int):
    """Проверяет, зарегистрирован ли пользователь.

    Args:
        user_id (int): Идентификатор пользователя.

    Returns:
        bool: True, если пользователь зарегистрирован, False в противном случае.
    """
    return UserRegistration.select().where(
        UserRegistration.user_id == user_id).exists()


def save_user_registration(user_id: int, user_name: str) -> bool:
    """Сохраняет регистрацию пользователя в базе данных.

    Args:
        user_id (int): Идентификатор пользователя.
        user_name (str): Имя пользователя.

    Returns:
        bool: True, если регистрация прошла успешно,
              False в противном случае.
    """
    try:
        new_user = UserRegistration.create(
            user_id=user_id,
            user_name=user_name,
            favorite_movies='[]',
            registration_date=datetime.now()
        )
        return True

    except Exception as exc:
        logger.error(
            f'Ошибка при сохранении регистрации пользователя {user_id}: {exc}'
        )
        return False
    

def get_user_name(user_id):
    try:
        user = UserRegistration.select().where(
            UserRegistration.user_id == user_id).first()
        if user:
            return user.user_name
        
    except Exception as exc:
        logger.error(
            f'Ошибка, пользователь отсутствует в базе: {exc}'
        )

def add_favorite_movie(user_id: int, movie_name: str) -> bool:
    """Добавляет фильм в избранное пользователя.

    Args:
        user_id (int): Идентификатор пользователя.
        movie_name (str): Название фильма.

    Returns:
        bool: True, если фильм успешно добавлен, 
        False в противном случае.
    """
    try:
        user = UserRegistration.get(UserRegistration.user_id == user_id)

        # Получение текущего списка избранных фильмов:
        favorite_movies_str = user.favorite_movies

        # Проверка на пустую строку и инициализация пустого списка:
        if not favorite_movies_str:
            favorite_movies = []
        else:
            favorite_movies = json.loads(favorite_movies_str)

        # Добавление нового фильма в список:
        favorite_movies.append(movie_name)

        # Сохранение обновленного списка обратно в базу данных:
        user.favorite_movies = json.dumps(favorite_movies)
        user.save()

        logger.info(
            f'Фильм "{movie_name}" добавлен в избранное пользователя с ID {user_id}.'
        )
        return True

    except Exception as exc:
        logger.error(
            f'Ошибка при добавлении фильма в избранное: {exc}'
        )
        return False

def get_favorite_movie(user_id: int) -> list:
    """Получает список избранных фильмов пользователя.

    Args:
        user_id (int): Идентификатор пользователя.

    Returns:
        list: Список названий избранных фильмов.
    """
    try:
        user = UserRegistration.get(UserRegistration.user_id == user_id)
        # Получение текущего списка избранных фильмов:
        favorite_movies_str = user.favorite_movies

        # Проверка на пустую строку и возврат пустого списка:
        if not favorite_movies_str:
            return []
        
        favorite_movies = json.loads(favorite_movies_str)
        return favorite_movies
    except Exception as exc:
        logger.error(
            f'Ошибка при получении избранных фильмов: {exc}'
        )
        return []

def get_user_history(user_id: int) -> str:
    """Получает историю пользователя, включая избранные фильмы.

    Args:
        user_id (int): Идентификатор пользователя.

    Returns:
        str: История пользователя.
    """
    try:
        user = UserRegistration.get(UserRegistration.user_id == user_id)
        favorite_movies_str = user.favorite_movies
        if favorite_movies_str:
            favorite_movies = json.loads(favorite_movies_str)
        else:
            favorite_movies = []

        history = (f'🆔 Имя пользователя: {user.user_name}\n\n'
                   f'✅ Дата регистрации: {user.registration_date}\n\n'
                   f'⭐ Избранные фильмы:\n\n'
        )
        history += '\n'.join(
            favorite_movies
        ) if favorite_movies else 'Нет избранных фильмов.'
        return history

    except UserRegistration.DoesNotExist:
        logger.error(f'Пользователь с ID {user_id} не найден.')
        return 'Пользователь не найден.'
    
    except Exception as exc:
        logger.error(f'Ошибка при получении истории пользователя: {exc}')
        return 'Произошла ошибка при получении истории.'

def remove_favorite_name(user_id: int, movie_name: str) -> bool:
    """
    Удаляет фильм из избранного пользователя.

    Args:
        user_id (int): Идентификатор пользователя.
        movie_name (str): Название фильма для удаления.

    Returns:
        bool: True, если фильм успешно удален, False в противном случае.
    """
    try:
        user = UserRegistration.get(UserRegistration.user_id == user_id)
        favorite_movies_str = user.favorite_movies

        if favorite_movies_str:
            favorite_movies = json.loads(favorite_movies_str)
        else:
            favorite_movies = []
        
        if movie_name in favorite_movies:
            favorite_movies.remove(movie_name)
            user.favorite_movies = json.dumps(favorite_movies)
            user.save()
            return True
        else:
            return False
        
    except UserRegistration.DoesNotExist:
        logger.error(f'Пользователь с ID {user_id} не найден.')
        return False
    except Exception as exc:
        logger.error(f'Ошибка при удалении фильма из избранного: {exc}')
        return False


