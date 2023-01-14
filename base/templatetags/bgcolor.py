from django import template
from dashboard.models import Design
register = template.Library()

@register.simple_tag
def color():
    return Design.objects.get(id=1).color

@register.simple_tag
def font_color():
    return Design.objects.get(id=1).font_color