from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings

BOT_NAME = "78ru"

SPIDER_MODULES = ["seventy_eight_ru.spiders"]
NEWSPIDER_MODULE = "seventy_eight_ru.spiders"

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS_PER_DOMAIN = 5

FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    "seventy_eight_ru.pipelines.DBPipeline": 300,
}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"


class Settings(BaseSettings):
    pg_db: str
    pg_user: str
    pg_pass: SecretStr
    pg_host: str
    pg_port: int

    export_to_json: bool
    export_path: Path
    parsing_period_minutes: int

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

if settings.export_to_json:
    json_pipe = "seventy_eight_ru.pipelines.JSONPipeline"
    ITEM_PIPELINES[json_pipe] = 1000
