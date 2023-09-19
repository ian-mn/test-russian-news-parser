import hashlib
from datetime import datetime
from uuid import UUID

from seventy_eight_ru.settings import BOT_NAME, settings


def generate_file_name() -> str:
    """Returns file path in folder/project_YYYY-MM-DD_HH:MM.json format."""
    now = datetime.now()
    dt_str = now.strftime("%Y-%m-%d_%H:%M")
    return settings.export_path / f"{BOT_NAME}_{dt_str}.json"


months = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}


def get_dt_from(time_str: str, date_str: str) -> datetime:
    "Converts '18:26' and '19 сентября 2023' to datetime."
    hour, minute = map(int, time_str.split(":"))

    day, month_ru, year = date_str.split(" ")
    month = months[month_ru]
    year, month, day = map(int, (year, month, day))

    return datetime(year, month, day, hour, minute)


def get_uuid(url: str) -> UUID:
    """Converts URL to MD5 UUID."""
    hash = hashlib.md5(url.encode("utf-8"))
    return UUID(hash.hexdigest())
