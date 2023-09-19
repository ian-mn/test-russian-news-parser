import os
from time import sleep

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from seventy_eight_ru.settings import settings


def run_spider() -> None:
    os.system("scrapy crawl 78ru")


if __name__ == "__main__":
    sleep(5)
    run_spider()

    scheduler = BlockingScheduler()

    trigger = IntervalTrigger(
        minutes=settings.parsing_period_minutes,
    )
    scheduler.add_job(
        run_spider,
        trigger=trigger,
        name="78ru parsing job",
    )
    scheduler.start()
