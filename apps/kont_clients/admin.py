from django.contrib import admin
from apps.kont_clients.models import KontentorClient
from apps.kont_system.admin import KontentorModelAdmin

@admin.register(KontentorClient)
class KontentorClientAdmin(KontentorModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "url",
    )
    search_fields = ("name", "email", "phone")
    list_filter = ("name",)
