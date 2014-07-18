from django import template
import numpy

register = template.Library()

@register.filter(name='avg')
def avg(values):
    """Returns the average value of a list"""
    return sum(values, 0)/len(values)

@register.filter(name='max')
def list_max(values):
    """Returns the max value of a list"""
    return max(values)

@register.filter(name='min')
def list_min(values):
    """Returns the min value of a list"""
    return min(values)

@register.filter(name='stddev')
def stddev(values):
    """Returns the average value of a list"""
    sum = 0.0
    for item in values:
        sum = sum + float(item)
    return numpy.std(values)

@register.filter(name='xrange_tag')
def xrange_tag(start, end):
    """Returns an xrange from CSV"""
    return xrange(start, end)
	
@register.filter(name='value_at')
def value_at(values, index):
	"""Returns the dict value at a key"""
	index = index - 1
	if index < len(values) and index >= 0:
		return values[index]
	else:
		return ''

@register.filter(name='racer_min')
def racer_min(racer):
	laps = racer.lap_set.values_list('time', flat=True)
	return min(laps)
	
@register.filter(name='racer_avg')
def racer_avg(racer):
	laps = racer.lap_set.values_list('time', flat=True)
	return sum(laps)/len(laps)

@register.filter(name='time_format')
def time_format(time):
	return "{:.3f}".format(time)
