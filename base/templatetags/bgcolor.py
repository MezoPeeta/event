from django import template
from dashboard.models import Design
from django.core.cache import cache
register = template.Library()

@register.simple_tag
def color():

    if cache.get('color'):
        color = cache.get('color')
        print('Got from cache')
    else:
        color = Design.objects.get(id=1).color
        cache.set('color',color)
        print('Got from database')
    return color


@register.simple_tag
def font_color():
    try:
        font_color,_ = Design.objects.get(id=1)[0].font_color
    except:
        font_color = '#ffffff'
    return font_color