from apps.kont_system.models import KontentorSiteSettings


def site_settings(request):
    """
    Получение параметров сайта
    """
    settings = KontentorSiteSettings.objects.first()

    return {"site_settings": settings}
