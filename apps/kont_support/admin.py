from django.contrib import admin

from apps.kont_support.models import KontentorQuestion, KontentorTicket
from apps.kont_system.admin import KontentorModelAdmin


@admin.register(KontentorTicket)
class KontentorTicketAdmin(KontentorModelAdmin):
    list_display = ("title", "status", "priority", "created_at", "updated_at")
    list_filter = ("status", "priority")
    search_fields = ("title", "description")
    ordering = ("-created_at",)


@admin.register(KontentorQuestion)
class KontentorQuestionAdmin(KontentorModelAdmin):
    list_display = ("title",)
