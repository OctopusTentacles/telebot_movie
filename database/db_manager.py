


from models import UserRequest
from peewee import IntegrityError


def save_user_registration(user_id, user_name):
    try:
        UserRequest.create(
            user_id = user_id,
            user_name = user_name,
            category = 'registration'
        )
    except IntegrityError: