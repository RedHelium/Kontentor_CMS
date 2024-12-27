from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-1ljip3x#y-^oia%lka9+(ksb(3&x%1c6r_m=h&5)3k&-=lv^$r"

DEBUG = True

ADMIN_SITE_HEADER = "Мой сайт"
ADMIN_SITE_TITLE = "Мой сайт"

ALLOWED_HOSTS = ["127.0.0.1"]

AUTH_USER_MODEL = "kont_users.KontentorUser"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "adminsortable2",
    "tinymce",
    "django_ace",
    "apps.kont_system",
    "apps.kont_users",
    "apps.kont_pages",
    "apps.kont_media",
    "apps.kont_support",
    "apps.kont_clients",
    "apps.kont_deals",
    "apps.kont_blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "kontentor.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.kont_system.context_processors.site_settings",
                "apps.kont_pages.context_processors.navigation",
                "apps.kont_pages.context_processors.footer",
            ],
        },
    },
]

WSGI_APPLICATION = "kontentor.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "kontentor",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "PORT": 5433,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Vladivostok"

USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

TINYMCE_DEFAULT_CONFIG = {
    "height": 600,
    "width": 1200,
    "menubar": True,
    "plugins": [
        "advlist",
        "autolink",
        "lists",
        "link",
        "image",
        "editimage" "charmap",
        "media",
        "mediaembed",
        "preview",
        "anchor",
        "visualblocks",
        "code",
        "codesample",
        "fullscreen",
        "insertdatetime",
        "table",
        "paste",
        "help",
        "wordcount",
        "accordion",
        "emoticons",
        "quickbars",
        "searchreplace",
    ],
    "toolbar1": "undo redo | styles fontfamily fontsize bold italic strikethrough underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent subscript superscript",
    "toolbar2": "copy cut paste | media image link table | hr emoticons",
    'codesample_languages': [
        {'text': 'HTML/XML', 'value': 'html'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'Python', 'value': 'python'},
    ]
}