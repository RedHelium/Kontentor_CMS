from django.db import models
from tinymce.models import HTMLField
from apps.kont_pages.models import KontentorPage
from apps.kont_users.models import KontentorUser


class KontentorTicketStatus(models.Model):
    """
    Статус тикета
    """

    code = models.CharField(
        verbose_name="Код статуса",
        blank=False,
        null=False,
        default="unknown",
        unique=True,
        max_length=16,
    )
    label = models.CharField(
        verbose_name="Заголовок статуса",
        blank=False,
        null=False,
        default="Новый статус",
        max_length=32,
    )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Статус тикета"
        verbose_name_plural = "Статусы тикетов"


class KontentorTicketPriority(models.Model):
    """
    Приоритет тикета
    """

    code = models.CharField(
        verbose_name="Код приоритета",
        blank=False,
        null=False,
        default="unknown",
        unique=True,
        max_length=16,
    )
    label = models.CharField(
        verbose_name="Заголовок приоритета",
        blank=False,
        null=False,
        default="Новый",
        max_length=32,
    )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Приоритет тикета"
        verbose_name_plural = "Приоритеты тикетов"


class KontentorTicket(models.Model):
    """
    Тикет
    """

    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    status = models.ForeignKey(
        KontentorTicketStatus, on_delete=models.CASCADE, verbose_name="Статус"
    )

    priority = models.ForeignKey(
        KontentorTicketPriority, on_delete=models.CASCADE, verbose_name="Приоритет"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    creator = models.ForeignKey(
        KontentorUser, on_delete=models.CASCADE, verbose_name="Создатель"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"


class KontentorQuestion(models.Model):
    """
    Вопрос для FAQ
    """

    title = models.CharField(max_length=100, verbose_name="Вопрос")
    answer = HTMLField(
        default="Автоматически сгенерированный ответ",
        null=False,
        blank=False,
        verbose_name="Ответ",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ Вопрос"
        verbose_name_plural = "FAQ Вопросы"
