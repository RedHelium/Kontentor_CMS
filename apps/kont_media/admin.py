from django.contrib import admin

from apps.kont_system.admin import KontentorModelAdmin
from .models import KontentorMediaFile
from django.utils.safestring import mark_safe


@admin.register(KontentorMediaFile)
class MediaFileAdmin(KontentorModelAdmin):
    list_display = ("image_preview", "file", "created_at")
    search_fields = ("file",)
    list_filter = ("created_at",)

    def image_preview(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}"  width="100" height="100" class="img-fluid rounded  border border-light border-2">')
        else:
            return obj.file.id

    image_preview.short_description = "Превью файла"
