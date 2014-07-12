from django import template

register = template.Library()

@register.filter(name='avg')
def avg(values):
    """Returns the average value of a list"""
    sum = 0.0
    for item in values:
        sum = sum + float(item)
    return sum/len(values)

@register.filter(name='max')
def max(values):
    """Returns the max value of a list"""
    max = values[0]
    for item in values:
        if item > max:
            max = item
    return max

@register.filter(name='min')
def min(values):
    """Returns the min value of a list"""
    min = values.first
    for item in values:
        if item < min:
            min = item
    return min

@register.filter(name='stddev')
def stddev(values):
    """Returns the average value of a list"""
    sum = 0.0
    for item in values:
        sum = sum + float(item)
    return sum/len(values)

@register.filter(name='xrange_tag')
def xrange_tag(start, end):
    """Returns an xrange from CSV"""
    return xrange(start, end)