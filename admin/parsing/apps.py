from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ParsingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "parsing"
    verbose_name = _("parsings")
