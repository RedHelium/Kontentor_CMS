from django.db import models


class SingletonModel(models.Model):
    """
    Singleton
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get(pk=1)
        except cls.DoesNotExist:
            return cls.objects.create(pk=1)


class KontentorSiteSettings(SingletonModel):
    """
    Настройки сайта
    """

    # Основные параметры

    title = models.CharField(
        verbose_name="Название сайта",
        default="Сайт создан при помощи Контентора",
        max_length=100,
    )

    # Блок метаданных
    meta_title = models.CharField(
        verbose_name="Заголовок сайта в метаданных",
        default="Сайт создан при помощи Контентора",
        max_length=200,
    )
    meta_description = models.CharField(
        verbose_name="Описание сайта в метаданных",
        default="Данный сайт создан при помощи Контентора - отечественной CMS на Django.",
        max_length=600,
    )
    meta_keywords = models.CharField(
        verbose_name="Ключевые слова сайта в метаданных",
        blank=True,
        null=True,
        max_length=200,
    )
    meta_encoding = models.CharField(
        help_text='Если вы не знаете для чего этот параметр - оставьте значение по умолчанию. Значение по умолчанию - "utf-8"',
        verbose_name="Кодировка сайта в метаданных",
        default="utf-8",
        max_length=16,
    )
    meta_viewport = models.CharField(
        verbose_name="Масштаб отображения страницы в метаданных",
        default="width=device-width, initial-scale=1.0",
        help_text='Если вы не знаете для чего этот параметр - оставьте значение по умолчанию. Значение по умолчанию - "width=device-width, initial-scale=1.0"',
        max_length=48,
    )
    meta_robots = models.CharField(
        verbose_name="Правила загрузки и индексирования страниц в метаданных роботами",
        default="index,follow",
        help_text='Если вы не знаете для чего этот параметр - оставьте значение по умолчанию. Значение по умолчанию - "index,follow"',
        max_length=64,
    )
    meta_language = models.CharField(
        verbose_name="Код языка", default="ru", max_length=2
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Параметры сайта"
        verbose_name_plural = "Параметры сайта"


# TODO Протестировать на заполнение
class KontentorOpenGraphDataPage(models.Model):
    """
    Open Graph теги
    """

    page = models.ForeignKey(
        "kont_pages.KontentorPage",
        verbose_name="Страница",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        verbose_name="Заголовок объекта", default="", blank=True, null=True, max_length=150
    )
    # TODO Сделать выпадающим меню
    type = models.CharField(
        verbose_name="Тип объекта", default="website", max_length=16
    )
    url_image = models.URLField(
        verbose_name="Ссылка на изображение в посте",
        blank=True,
        null=True,
        max_length=150,
    )
    width_image = models.CharField(
        verbose_name="Ширина изображения в пикселях",
        blank=True,
        null=True,
        max_length=4,
    )
    height_image = models.CharField(
        verbose_name="Высота изображения в пикселях",
        blank=True,
        null=True,
        max_length=4,
    )
    description = models.CharField(
        verbose_name="Описание объекта", blank=True, null=True, max_length=300
    )
    url = models.URLField(
        verbose_name="URL-адрес, который ведёт к объекту",
        blank=True,
        null=True,
        max_length=200,
    )
    site_name = models.CharField(
        verbose_name="Название сайта, которое будет отображаться на всех страницах",
        blank=True,
        null=True,
        max_length=150,
    )

    facebook_app_id = models.CharField(
        verbose_name="Уникальный идентификатор Facebook",
        blank=True,
        null=True,
        max_length=150,
    )

    twitter_title = models.CharField(
        verbose_name="Заголовок объекта для X/Twitter",
        blank=True,
        null=True,
        max_length=150,
    )
    twitter_url = models.URLField(
        verbose_name="URL-адрес, который ведёт к объекту для X/Twitter",
        blank=True,
        null=True,
        max_length=200,
    )
    twitter_description = models.CharField(
        verbose_name="Описание объекта для X/Twitter",
        blank=True,
        null=True,
        max_length=300,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Open Graph тэги"
        verbose_name_plural = "Open Graph тэги"
