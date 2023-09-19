"""Django settings for config project."""

from split_settings.tools import include

include(
    "components/main_settings.py",
    "components/apps.py",
    "components/database.py",
    "components/localization.py",
    "components/validation.py",
    "components/logging.py",
)
