from django.contrib import admin

from apps.kont_blog.models import (
    KontentorBlogArticle,
    KontentorBlogCategory,
    KontentorBlogTag,
)
from apps.kont_system.admin import KontentorModelAdmin


@admin.register(KontentorBlogCategory)
class KontentorBlogCategoryAdmin(KontentorModelAdmin):
    """
    Админка для категорий
    """

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(KontentorBlogTag)
class KontentorBlogTagAdmin(KontentorModelAdmin):
    """
    Админка для тегов
    """

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(KontentorBlogArticle)
class KontentorBlogArticleAdmin(KontentorModelAdmin):
    """
    Админка для статей
    """

    list_display = (
        "title",
        "category",
        "author",
        "created_at",
        "updated_at",
        "is_published",
    )
    search_fields = ("title", "content", "category__name", "author__username")
    list_filter = ("category", "tags", "author", "is_published")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    verbose_name = "Статья"
    verbose_name_plural = "Статьи"
    filter_horizontal = ("tags",)
    readonly_fields = ("created_at", "updated_at")
