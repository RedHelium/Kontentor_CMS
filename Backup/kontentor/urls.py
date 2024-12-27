from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "kt-admin/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path("kt-admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("", include("apps.kont_users.urls")),
    path("", include("apps.kont_pages.urls")),
    path("", include("apps.kont_media.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
