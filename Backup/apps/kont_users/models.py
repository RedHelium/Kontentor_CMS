from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.kont_users.utils.managers import KontentorUserManager
from django.contrib.auth.models import Group


class KontentorUserGroup(Group):
    """
    Группа пользователей
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Группа пользователей"
        verbose_name_plural = "Группы пользователей"


class KontentorUser(AbstractUser):
    """
    Пользователь
    """

    username = None
    email = models.EmailField(verbose_name="Email", unique=True)
    groups = models.ManyToManyField(
        KontentorUserGroup,
        related_name="kt_user_groups",
        blank=True,
        verbose_name="Группа",
    )

    objects = KontentorUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
