# Generated by Django 4.2.2 on 2023-09-19 10:51

from django.db import migrations, models
from ckeditor.fields import RichTextField


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL("CREATE SCHEMA IF NOT EXISTS content;"),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "post_id",
                    models.UUIDField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("post_url", models.URLField(verbose_name="post_url")),
                ("post_title", models.CharField(verbose_name="post_title")),
                ("post_text", RichTextField(verbose_name="post_text")),
                ("date_create", models.DateTimeField(null=False, blank=False)),
            ],
            options={
                "verbose_name": "Posts",
                "verbose_name_plural": "Post",
                "db_table": 'content"."posts',
            },
        ),
    ]