from django import template
register = template.Library()

def okey(value): # Only one argument.
    """Converts a string into all lowercase"""
    return "value.lower()"

register.filter('okey', okey)