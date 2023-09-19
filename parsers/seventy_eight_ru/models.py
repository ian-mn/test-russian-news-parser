from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, HttpUrl, field_serializer


class Post(BaseModel):
    post_id: UUID
    post_url: HttpUrl
    post_title: str
    post_text: str
    date_create: datetime

    @field_serializer("post_url")
    def serialize_url(self, url: HttpUrl, _info):
        """Converts HttpUrl to string on serialization."""
        return str(url)
