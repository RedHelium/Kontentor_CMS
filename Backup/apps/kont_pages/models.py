import os
from django.db import models
from django.template.loader import get_template
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class KontentorPage(models.Model):
    """
    Страница
    """

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, unique=True, verbose_name="ЧПУ (URL)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(
        verbose_name="Опубликовано", blank=False, null=False, default=False
    )

    def __str__(self):
        return self.title
      

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class KontentorPageBlock(models.Model):
    """
    Блок контента на странице
    """

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    code = models.CharField(
        max_length=32,
        verbose_name="Код блока",
        blank=False,
        null=False,
        unique=True,
        help_text="Код должен быть на английском",
    )
    page = models.ForeignKey(
        KontentorPage,
        verbose_name="Страница",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        default="",
        null=False,
        blank=False,
        verbose_name="Контент блока",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(
        verbose_name="Отображать", blank=False, null=False, default=False
    )
    is_cross_page_block = models.BooleanField(
        verbose_name="Отображать блок на каждой странице?",
        blank=False,
        null=False,
        default=False,
    )
    order = models.PositiveIntegerField(
        verbose_name="Приоритет отображения", blank=False, null=False, default=0
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwagrs):

        with open(
            "%s/custom/%s.html"
            % (os.path.join(os.path.dirname(__file__), "templates"), self.code),
            "w",
            encoding="utf-8",
        ) as file:
            file.write(self.content)

        return super().save(*args, **kwagrs)

    # BUG Функция удаления не выполняется при массовом удалении элементов (через страницу со списком элементов)
    def delete(self, *args, **kwargs):

        file_path = "%s/custom/%s.html" % (
            os.path.join(os.path.dirname(__file__), "templates"),
            self.code,
        )

        if os.path.exists(file_path):
            os.remove(file_path)

        super().delete(*args, **kwargs)

    def rendered_template(self, request):
        template = get_template(
            "%s/custom/%s.html"
            % (os.path.join(os.path.dirname(__file__), "templates"), self.code)
        )
        context = {}
        items = KontentorPageBlockContextItem.objects.filter(pageBlock=self.id)

        get_params = request.GET

        if items is not None and len(items) > 0:
            for item in items:

                if len(get_params) > 0:
                    for param in get_params:
                        if param in item.code:
                            value = get_params.get(param)
                            context[item.code] = item.get_models(id=value)
                        else:
                            context[item.code] = item.get_models()
                else:
                    context[item.code] = item.get_models()

        return template.render(context)

    class Meta:
        verbose_name = "Блок страницы"
        verbose_name_plural = "Блоки страниц"
        ordering = ["order"]


class KontentorPageBlockContextItem(models.Model):
    """
    Контекст данных, подгружаемый для блока страниц
    """

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name="Данные"
    )
    # object_id = models.PositiveIntegerField()
    content_object = GenericRelation(
        "KontentorPageBlockContextItem",
        related_query_name="KontentorContextPageBlockItems",
    )
    pageBlock = models.ForeignKey(
        KontentorPageBlock,
        on_delete=models.CASCADE,
        verbose_name="Блок страницы",
        blank=False,
        null=False,
    )
    code = models.CharField(
        max_length=32, verbose_name="Код контекста", blank=False, null=False, default=""
    )

    def _get_related_model(self):
        return self.content_type.model_class()

    def get_models(self, *args, **kwargs):
        return self._get_related_model().objects.filter(*args, **kwargs)

    class Meta:
        verbose_name = "Контекст блока страницы"
        verbose_name_plural = "Контекст блоков страниц"


class KontentorMenuItem(models.Model):
    """
    Пункт меню
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок меню")
    page = models.ForeignKey(
        KontentorPage,
        verbose_name="Страница",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Родительский пункт меню",
        related_name="children",
    )
    order = models.PositiveIntegerField(
        verbose_name="Приоритет отображения", blank=False, null=False, default=0
    )
    is_published = models.BooleanField(
        verbose_name="Опубликовано", blank=False, null=False, default=False
    )
    is_show_on_navigation = models.BooleanField(
        verbose_name="Отображать в навигации сайта",
        blank=False,
        null=False,
        default=True,
    )
    is_show_on_footer = models.BooleanField(
        verbose_name="Отображать в подвале сайта",
        blank=False,
        null=False,
        default=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт меню навигации"
        verbose_name_plural = "Пункты меню навигации"
        ordering = ["order"]
