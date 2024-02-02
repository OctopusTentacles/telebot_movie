import os
import sys

from dotenv import find_dotenv
from dotenv import load_dotenv


if find_dotenv is None:
    sys.exit('Переменные окружения не загружены, так как отсутствует файл .env')
else:
    load_dotenv()


USERNAME = os.getenv('USERNAME')
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')