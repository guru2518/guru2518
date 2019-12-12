from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
	"""
	This cuts out all values of "arg" from the string !
	"""

	return value.replace(arg,'')

# register.filter('cut',cut) [this one option to register the filter or use decoraters. ]

