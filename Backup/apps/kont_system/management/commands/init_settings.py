from typing import Any
from django.core.management.base import BaseCommand
from apps.kont_system.models import KontentorSiteSettings


class Command(BaseCommand):
    """
    Команда инициализации параметров сайта
    """

    def handle(self, *args: Any, **options: Any) -> str | None:
        KontentorSiteSettings.objects.create()
