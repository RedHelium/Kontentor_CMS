from django.urls import path, re_path
from .views import KontentorPageView

urlpatterns = [
    re_path(r'^(?P<slug>.*)/$', KontentorPageView.as_view(),),
]
