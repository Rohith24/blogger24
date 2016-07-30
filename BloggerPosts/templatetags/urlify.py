from django import template
from urllib import quote_plus
register = template.Library()

@register.filter
def urlify(value):
    return quote_plus(value)
