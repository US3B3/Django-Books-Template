from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value, arg1):
    return value.replace(arg1," ")

@register.simple_tag(name='degis')
def degis(value, arg1, arg2):
    return value.replace(arg1,arg2)

@register.filter(name='splitList')
def splitList(value, arg1):
    return value.split(arg1)