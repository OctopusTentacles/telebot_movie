"""Модуль для работы с API.

Получает самый популярный фильм на сегодня.
"""


import requests

from io import BytesIO


def popular_today():
    url = 'https://api.kinopoisk.dev/v1.4/list/movies/popular-films'

{
  "category": "Фильмы",
  "name": "Популярные фильмы",
  "slug": "popular-films",
  "moviesCount": 1000,
  "cover": {
    "url": "https://avatars.mds.yandex.net/get-kinopoisk-image/1629390/5e785e92-af07-485c-b4b2-89b64b32c6d9/orig",
    "previewUrl": "https://avatars.mds.yandex.net/get-kinopoisk-image/1629390/5e785e92-af07-485c-b4b2-89b64b32c6d9/x1000"
  },
  "createdAt": "2023-09-23T20:05:14.042Z",
  "updatedAt": "2023-09-23T20:05:14.042Z"
}



    ...