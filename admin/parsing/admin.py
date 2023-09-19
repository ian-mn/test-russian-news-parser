from django.contrib import admin
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostInline(admin.TabularInline):
    model = Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "post_title",
        "date_create",
    )
    search_fields = ("post_title",)
    actions = ("export_selected",)

    @admin.action(description=_("Export selected posts"))
    def export_selected(self, request, queryset):
        """Exports selected rows to JSON."""
        selected = list(
            queryset.values_list(
                "post_id",
                "post_title",
                "post_text",
                "post_url",
                "date_create",
            )
        )
        return JsonResponse(
            selected,
            safe=False,
        )
