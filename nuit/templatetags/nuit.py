from django import template

register = template.Library()

@register.simple_tag
def set_active_menu(active_menu):
    return "<span style='display: none' class='nuit-active-menu'>%s</span>" % active_menu
