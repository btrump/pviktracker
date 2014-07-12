from django.db import models
from django.contrib.auth.models import User

class Racer(models.Model):
    display_name = models.CharField(max_length=70)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.display_name
    
    def absolute_url(self):
        return '/heats/%s/%s/%s/%s' % (self.day.year, self.day.month, self.day.day, self.number)

class Heat(models.Model):
    day = models.DateField(null=False, blank=False)
    number = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return '%s - Heat %s' % (self.day, self.number)
    
    def absolute_url(self):
        return '/heats/%s/%s/%s/%s' % (self.day.year, self.day.month, self.day.day, self.number)
        
    def racers(self):
        racers = Racer.objects.filter(pk__in=list(set(Lap.objects.filter(heat=self).values_list('racer', flat=True))))
        return racers
        
    def avg(self, racer):
        laps = Lap.objects.filter(heat=self, racer=racer)
        time = 0.0
        for lap in laps:
            time = time + lap.time
        return time/float(len(laps))
        
class Lap(models.Model):
	racer = models.ForeignKey(Racer)
	heat = models.ForeignKey(Heat)
	number = models.IntegerField(blank=False, null=False)
	time = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=3)

