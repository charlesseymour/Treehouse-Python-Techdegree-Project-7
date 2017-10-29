from django import template

register = template.Library()

@register.filter('verbose_name')
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name
    
@register.filter('get_attr')
def get_attr(obj, val): 
    return getattr(obj, val)