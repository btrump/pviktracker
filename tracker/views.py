from django.shortcuts import render_to_response
from django.template import RequestContext
from tracker.models import *
from django.contrib.auth.models import User
import datetime

def home(request, *args, **kwargs):
    context = RequestContext(request, kwargs)
    return render_to_response('index.html', context)
    
def heats(request, *args, **kwargs):
	if kwargs['number']:
		date = datetime.date(year=int(kwargs['year']), month=int(kwargs['month']), day=int(kwargs['day']))
		heat = Heat.objects.get(number=int(kwargs['number']), day=date)
		racers = heat.racers()
		laps = dict()
		most_laps = 0
		for racer in racers:
			racer_laps = Lap.objects.filter(heat=heat, racer=racer).order_by('number').values_list('time', flat=True)
			laps[racer] = racer_laps
			if len(racer_laps) > most_laps:
				most_laps = len(racer_laps)
		
		instance = {'heat': heat, 'racers': racers, 'laps': laps, 'column_count': len(racers)+1, 'most_laps': most_laps, 'most_laps_range': xrange(1, most_laps+1)}
		context = RequestContext(request, instance)
		return render_to_response('heats/detail.html', context)
	else:
		# in absence of heat number, show all heats in this date range
		if kwargs['year']:
			if kwargs['day']:
				date_start = datetime.date(year=int(kwargs['year']), month=int(kwargs['month']), day=int(kwargs['day']))
				date_end = date_start
			elif kwargs['month']:
				date_start = datetime.date(year=int(kwargs['year']), month=int(kwargs['month']), day=1)
				date_end = datetime.date(year=int(kwargs['year']), month=int(kwargs['month']), day=28)
			else:
				date_start = datetime.date(year=int(kwargs['year']), month=1, day=1)
				date_end = datetime.date(year=int(kwargs['year']), month=12, day=28)
			heats = Heat.objects.filter(day__gte=date_start, day__lte=date_end)
		else:
			heats = Heat.objects.all()			
		instance = {'heats':heats, 'kwargs':kwargs}
		context = RequestContext(request, instance)
		return render_to_response('heats/list.html', context)
