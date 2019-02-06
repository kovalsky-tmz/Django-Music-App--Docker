from django import template

register = template.Library()

@register.filter
def space(value):
    return value.replace(".mp3"," ").replace("_"," ")