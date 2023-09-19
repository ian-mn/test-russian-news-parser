"""Database settings."""

import os

from dotenv import load_dotenv

load_dotenv()


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("pg_db"),
        "USER": os.environ.get("pg_user"),
        "PASSWORD": os.environ.get("pg_pass"),
        "HOST": os.environ.get("pg_host", "db"),
        "PORT": os.environ.get("pg_port", 5432),
        "OPTIONS": {"options": "-c search_path=public,content"},
    }
}
