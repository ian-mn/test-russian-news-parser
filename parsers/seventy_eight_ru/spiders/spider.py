from urllib.parse import urljoin

from scrapy import Request, Spider
from scrapy_playwright.page import PageMethod
from seventy_eight_ru.models import Post
from seventy_eight_ru.utils import get_dt_from, get_uuid


class PostsSpider(Spider):
    name = "78ru"
    allowed_domains = ["78.ru"]
    start_url = "https://78.ru/news"
    base_url = "https://78.ru"

    def start_requests(self):
        """Requests self.start_url."""
        yield Request(
            url=self.start_url,
            callback=self.get_posts,
            meta=dict(
                playwright=True,
                playwright_page_methods=[
                    PageMethod(
                        "wait_for_selector",
                        "a.news-feed-timeline-item",
                        timeout=60000,
                    )
                ],
            ),
        )

    def get_posts(self, response):
        """Gets start page, requests news urls."""
        links = response.css(".news-feed-timeline-item").xpath("@href").getall()
        for link in links:
            yield Request(
                url=urljoin(self.base_url, link),
                callback=self.get_post,
                meta=dict(
                    playwright=True,
                ),
            )

    def get_post(self, response):
        """Gets Post date from news URL."""
        title = response.css("h1::text").get()
        time_str, date_str = response.css(".author-and-date__segment::text").getall()
        dt = get_dt_from(time_str, date_str)
        text = response.css(".news__inner").get()

        yield Post(
            post_id=get_uuid(response.url),
            post_title=title,
            post_text=text,
            post_url=response.url,
            date_create=dt,
        )
