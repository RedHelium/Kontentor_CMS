from django import template

register = template.Library()


@register.filter(is_safe=True)
def get_published_childs(items, parent):
    return items.filter(parent=parent, is_published=True, is_show_on_navigation=True)
