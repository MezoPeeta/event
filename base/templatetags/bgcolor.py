from django import template
from dashboard.models import Design
register = template.Library()

@register.simple_tag
def color():
    try:
        color = Design.objects.get(id=1).color
    except:
        color = '#ff2a2a'
    return color

@register.simple_tag
def font_color():
    try:
        font_color = Design.objects.get(id=1).font_color
    except:
        font_color = '#ffffff'
    return font_color