from django import forms
from django.contrib import admin
from apps.kont_system.admin import KontentorModelAdmin
from apps.kont_users.models import KontentorUser, KontentorUserGroup
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(KontentorUserGroup)
class KontentorUserGroupAdmin(KontentorModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("permissions",)


class KontentorUserChangeFormAdmin(UserChangeForm):
    """
    Форма для редактирования пользователя
    """

    password = forms.CharField(
        widget=forms.PasswordInput, required=False, label="Пароль"
    )

    class Meta:
        model = KontentorUser
        fields = "__all__"

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(KontentorUser)
class KontentorUserAdmin(KontentorModelAdmin):
    form = KontentorUserChangeFormAdmin

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Личная информация", {"fields": ("first_name", "last_name")}),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Даты", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_login",)
    filter_horizontal = ("groups", "user_permissions")
    readonly_fields = (
        "last_login",
        "date_joined",
    )
