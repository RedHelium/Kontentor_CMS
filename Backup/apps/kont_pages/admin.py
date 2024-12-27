from django.contrib import admin
from django_ace import AceWidget
import os
from apps.kont_system.admin import (
    KontentorModelAdmin,
    KontentorStackedInline,
)
from apps.kont_system.models import KontentorOpenGraphDataPage
from .models import (
    KontentorMenuItem,
    KontentorPage,
    KontentorPageBlock,
    KontentorPageBlockContextItem,
)
from adminsortable2.admin import SortableAdminMixin


HTML_CODE_ACE_WIDGET = AceWidget(
    mode="django",
    width="1200px",
    height="600px",
    theme="one_dark",
    wordwrap=True,
    toolbar=False,
    fontsize="16px",
    showprintmargin=False,
)


class KontentorOpenGraphDataPageInline(KontentorStackedInline):
    model = KontentorOpenGraphDataPage
    max_num = 1
    classes = ["collapse"]


class KontentorPageBlockInline(KontentorStackedInline):
    model = KontentorPageBlock
    extra = 0
    classes = ["collapse"]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "content":
            kwargs["widget"] = HTML_CODE_ACE_WIDGET
        return super(KontentorStackedInline, self).formfield_for_dbfield(
            db_field, **kwargs
        )


class KontentorPageBlockContextItemInline(KontentorStackedInline):
    model = KontentorPageBlockContextItem
    extra = 0
    classes = ["collapse"]


@admin.register(KontentorPage)
class KontentorPageAdmin(KontentorModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    search_fields = (
        "title",
        "slug",
    )
    prepopulated_fields = {"slug": ("title",)}
    inlines = [KontentorPageBlockInline, KontentorOpenGraphDataPageInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            super().save_model(request, obj, form, change)
            KontentorOpenGraphDataPage.objects.create(page=obj)
        else:
            super().save_model(request, obj, form, change)


@admin.register(KontentorMenuItem)
class KontentorMenuItemAdmin(SortableAdminMixin, KontentorModelAdmin):
    list_display = (
        "order",
        "title",
        "page",
        "parent",
    )
    search_fields = ("title",)
    list_filter = ("title",)


@admin.register(KontentorPageBlock)
class KontentorPageBlockAdmin(SortableAdminMixin, KontentorModelAdmin):
    list_display = (
        "order",
        "title",
        "page",
    )
    search_fields = ("title",)
    list_filter = ("title", "page")
    inlines = [
        KontentorPageBlockContextItemInline,
    ]

    def save_model(self, request, obj, form, change):

        if change:

            try:
                previous_instance = KontentorPageBlock.objects.get(id=obj.id)
                old_template_path = "%s/custom/%s.html" % (
                    os.path.join(os.path.dirname(__file__), "templates"),
                    previous_instance.code,
                )
                new_template_path = "%s/custom/%s.html" % (
                    os.path.join(os.path.dirname(__file__), "templates"),
                    obj.code,
                )
                os.rename(old_template_path, new_template_path)

            except Exception as ex:
                raise ex

        super().save_model(request, obj, form, change)

    # Dracula, One Dark, Nord Dark, Tommorow Night, Twilight
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        widget = HTML_CODE_ACE_WIDGET

        form.base_fields["content"].widget = widget

        return form

    # def preview(self, obj):
    #     from django.utils.html import mark_safe

    #     return mark_safe(obj.content)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["preview"]
    #     return []


# @admin.register(KontentorPageBlockContextItem)
# class KontentorPageBlockContextItemAdmin(admin.ModelAdmin):
#     list_display = ("id",)
