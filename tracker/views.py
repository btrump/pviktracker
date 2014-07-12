from django.shortcuts import render_to_response
from django.template import RequestContext
from tracker.models import *
from django.contrib.auth.models import User
from datetime import date

def home(request, *args, **kwargs):
    context = RequestContext(request, kwargs)
    return render_to_response('index.html', context)
    
def heat_list(request, *args, **kwargs):
    heats = Heat.objects.all();
    context = RequestContext(request, {'heats':heats})
    return render_to_response('heats/list.html', context)

def heat_detail(request, *args, **kwargs):
    heat = Heat.objects.get(number=kwargs['heat']) #, day=date(kwargs['year'], kwargs['month'], kwargs['day']))
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
    return render_to_response('heats/detail.html', instance)

#
# def heat_detail(request, *args, **kwargs):
#     heat = Heat.objects.get(number=kwargs['heat']) #, day=date(kwargs['year'], kwargs['month'], kwargs['day']))
#     racers = User.objects.filter(pk__in=list(set(Lap.objects.filter(heat=heat).values_list('racer',flat=True))))
#
#     laps = []
#     most_laps = 0
#     for racer in racers:
#         racer_laps = Lap.objects.filter(heat=heat, racer=racer).order_by('number').values_list('time', flat=True)
#         laps.append(racer_laps)
#         if len(racer_laps) > most_laps:
#             most_laps = len(racer_laps)
#
#     instance = {'heat': heat, 'racers': racers, 'laps': laps, 'most_laps': xrange(1, most_laps+1)}
#     context = RequestContext(request, instance)
#     return render_to_response('heats/detail.html', instance)
#
