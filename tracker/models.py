from django.db import models
from django.contrib.auth.models import User

class Heat(models.Model):
    day = models.DateField(null=False, blank=False)
    number = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return '%s - Heat %s' % (self.day, self.number)
    
    def absolute_url(self):
        return '/heats/%s/%s/%s/%s' % (self.day.year, self.day.month, self.day.day, self.number)

class Lap(models.Model):
	racer = models.ForeignKey(User)
	heat = models.ForeignKey(Heat)
	number = models.IntegerField(blank=False, null=False)
	time = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=3)
