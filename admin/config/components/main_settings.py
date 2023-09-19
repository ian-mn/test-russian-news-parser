"""Main settings."""

import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("django_secret_key")

DEBUG = os.environ.get("debug", False) == "True"

mimetypes.add_type("application/javascript", ".js", True)

ALLOWED_HOSTS = os.environ.get("allowed_hosts", "127.0.0.1").split(",")

INTERNAL_IPS = ["127.0.0.1"]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIR = (os.path.join(BASE_DIR, "static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
