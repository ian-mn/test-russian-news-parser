"""Module with models for Parsing Admin Panel."""
import hashlib
from uuid import UUID

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    """Post model."""

    def __str__(self) -> str:
        return self.post_title

    post_id = models.UUIDField(primary_key=True, editable=False)
    post_url = models.URLField(_("post_url"), blank=False, null=False)
    post_title = models.CharField(_("post_title"), blank=False, null=False)
    post_text = RichTextField(_("post_text"), blank=False, null=False)
    date_create = models.DateTimeField(_("date_create"), null=False, blank=False)

    @property
    def get_post_id(self):
        """Converts URL to MD5 hash."""
        hash = hashlib.md5(self.post_url.encode("utf-8"))
        return UUID(hash.hexdigest())

    def save(self, *args, **kwargs):
        self.post_id = self.get_post_id
        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'content"."posts'
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
