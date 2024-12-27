from django.db import models
from apps.kont_users.models import KontentorUser
from tinymce.models import HTMLField


class KontentorBlogCategory(models.Model):
    """
    Категория статьи
    """

    name = models.CharField(
        max_length=150,
        unique=True,
        default="Новая категория",
        verbose_name="Категория статьи",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статьи"
        verbose_name_plural = "Категории статей"


class KontentorBlogTag(models.Model):
    """
    Тег статьи
    """

    name = models.CharField(
        max_length=64,
        unique=True,
        default="Новый тег",
        verbose_name="Тег статьи",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег статьи"
        verbose_name_plural = "Теги статьи"


class KontentorBlogArticle(models.Model):
    """
    Статья
    """

    title = models.CharField(max_length=100, verbose_name="Заголовок статьи")
    content = HTMLField(verbose_name="Содержание статьи")
    category = models.ForeignKey(
        KontentorBlogCategory, on_delete=models.CASCADE, verbose_name="Категория статьи"
    )
    tags = models.ManyToManyField(KontentorBlogTag, verbose_name="Теги статьи")
    author = models.ForeignKey(
        KontentorUser,
        on_delete=models.CASCADE,
        verbose_name="Автор статьи",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    published_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата публикации"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликована")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]
