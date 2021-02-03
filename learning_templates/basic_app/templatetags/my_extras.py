from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

#Pass as a string what i call the function and in second the function
register.filter('cut',cut)
