from django import template

register = template.Library()

@register.filter
def to(value):
    if isinstance(value, int):
        return range(value)
    return []