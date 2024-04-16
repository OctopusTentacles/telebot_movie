""" Модуль проверки регистрации пользователей. """


from datetime import datetime
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
            favorite_movies='',
            registration_date=datetime.now()
        )
        print('Пользователь успешно зарегистрирован')
        return True

    except Exception as exc:
        print('Ошибка в базе данных:', exc)
        return False
    

def get_user_name(user_id):
    try:
        user = UserRegistration.select().where(
            UserRegistration.user_id == user_id).first()
        if user:
            return user.user_name
        
    except Exception as exc:
        print(f"Error fetching user name: {exc}")
