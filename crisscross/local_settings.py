import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "crisscross",
        "USER": "game",
        "PASSWORD": "mygame",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
