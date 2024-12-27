from django.db import models


class KontentorMediaFile(models.Model):
    """
    Медиа-файл
    """

    file = models.FileField(verbose_name="Файл", upload_to="%Y/%m/%d")
    created_at = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)
    alt = models.CharField(
        max_length=150,
        verbose_name="Альтернативный текст",
        blank=True,
        null=True,
        default="",
    )
    title = models.CharField(
        max_length=150,
        verbose_name="Доп. информация о изображении при наведении",
        blank=True,
        null=True,
        default="",
    )

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = "Медиафайл"
        verbose_name_plural = "Медиафайлы"
