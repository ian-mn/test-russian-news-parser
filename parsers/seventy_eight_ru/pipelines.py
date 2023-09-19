import json

from seventy_eight_ru.database import Posts, get_session
from seventy_eight_ru.utils import generate_file_name


class DBPipeline:
    def open_spider(self, spider):
        self.session = get_session()

    def process_item(self, item, spider):
        exists = self.session.query(Posts).filter_by(post_id=item.post_id).first()
        if not exists:
            self.session.add(Posts(**item.model_dump()))
            self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()


class JSONPipeline:
    def open_spider(self, spider):
        self.items = []

    def process_item(self, item, spider):
        item_dict = item.model_dump()
        item_dict["post_id"] = str(item_dict["post_id"])
        item_dict["date_create"] = int(item_dict["date_create"].timestamp())
        self.items.append(item_dict)
        return item

    def close_spider(self, spider):
        with open(generate_file_name(), "w") as f:
            json.dump(
                self.items,
                f,
                ensure_ascii=True,
                indent=4,
            )
