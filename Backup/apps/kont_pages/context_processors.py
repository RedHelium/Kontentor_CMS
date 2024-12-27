from apps.kont_pages.models import KontentorMenuItem


def navigation(request):

    menu_items = KontentorMenuItem.objects.filter(
        is_published=True, is_show_on_navigation=True
    )

    return {"navigation_menu_items": menu_items}


def footer(request):

    menu_items = KontentorMenuItem.objects.filter(
        is_published=True, is_show_on_footer=True
    )

    return {"footer_menu_items": menu_items}
