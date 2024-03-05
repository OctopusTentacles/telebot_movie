"""Модуль для работы с API.

Получает актера/режиссера по имени, введенному пользователем.
"""


import requests


from config_data import config
from io import BytesIO
from log_data import logger


@logger.catch
def search_person_api(url):

    headers = {'accept': 'application/json', "X-API-KEY": config.API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contents = [data]
