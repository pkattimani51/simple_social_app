from django import template

register = template.Library()


@register.filter(name='timeconvert')
def local_time_conversion(value):
    return value