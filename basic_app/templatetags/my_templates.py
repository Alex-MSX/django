from django import template

register = template.Library()

@register.filter(name='custom_cut')
def custom_cut(value, arg):
    '''Esto quita arg de un string'''
    return value.replace(arg,'')
