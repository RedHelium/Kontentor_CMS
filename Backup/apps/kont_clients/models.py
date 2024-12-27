from django.db import models

from apps.kont_system.utils.fields import KontentorGenderField, KontentorPhoneField


# TODO Контактное лицо сделать в виде отдельной моделью + добавить inlines в панели админа
# TODO Добавить статус взаимоотношений с клиентом
# TODO Добавить категорию, добавить фильтрацию по категориям,
# статусам, сортировку - по наименованию, статусу, категории, дате создания, дате обновления
# TODO Добавить поле приоритета важности клиента
class KontentorClient(models.Model):

    name = models.CharField(
        max_length=100, verbose_name="Наименование", default="Новый клиент"
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = KontentorPhoneField(
        max_length=20, blank=True, null=True, verbose_name="Номер телефона"
    )
    url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="URL адрес"
    )
    contact_surname = models.CharField(
        max_length=32, blank=True, null=True, verbose_name="Фамилия контактного лица"
    )
    contact_firstname = models.CharField(
        max_length=32, blank=True, null=True, verbose_name="Имя контактного лица"
    )
    contact_patronymic = models.CharField(
        max_length=32, blank=True, null=True, verbose_name="Отчество контактного лица"
    )
    contact_gender = KontentorGenderField(verbose_name="Пол", blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name="Примечание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
