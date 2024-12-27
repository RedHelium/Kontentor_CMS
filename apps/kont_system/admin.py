from django.contrib import admin
from apps.kont_system.models import KontentorSiteSettings
from django.db import models
from django.forms import TextInput, CheckboxInput, Select, EmailInput, FileInput
from django.utils.safestring import mark_safe

HTML_FILE_PREVIEW = '<div class="row mx-auto"><div class="row mx-auto"><div class="col-auto"><img src="%s" class="img-fluid rounded rounded-1 shadow border border-light border-2"></div></div><div class="row mx-auto"><div class="col-auto"><a href="%s" target="_blank" class="mt-2 ps-3 pe-3 btn btn-primary text center">Скачать файл</a></div></div></div>'


class KontentorFilePreviewWidget(FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            url = value.url
            html = HTML_FILE_PREVIEW % (
                url,
                url,
            )
            return mark_safe(html)
        else:
            return super().render(name, value, attrs, renderer)


class KontentorStackedInline(admin.StackedInline):
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"class": "form-control"})},
        models.URLField: {"widget": TextInput(attrs={"class": "form-control"})},
        models.BooleanField: {
            "widget": CheckboxInput(attrs={"class": "form-check-input"})
        },
        models.ForeignKey: {
            "widget": Select(attrs={"class": "form-select form-select-sm"})
        },
        models.EmailField: {"widget": EmailInput(attrs={"class": "form-control"})},
        models.FileField: {"widget": KontentorFilePreviewWidget},
    }


class KontentorModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"class": "form-control"})},
        models.URLField: {"widget": TextInput(attrs={"class": "form-control"})},
        models.BooleanField: {
            "widget": CheckboxInput(attrs={"class": "form-check-input"})
        },
        models.ForeignKey: {
            "widget": Select(attrs={"class": "form-select form-select-sm"})
        },
        models.EmailField: {"widget": EmailInput(attrs={"class": "form-control"})},
        models.FileField: {"widget": KontentorFilePreviewWidget},
    }


@admin.register(KontentorSiteSettings)
class SiteSettingAdmin(KontentorModelAdmin):
    list_display = ("title",)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
