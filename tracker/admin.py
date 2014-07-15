from django.contrib import admin
from tracker.models import Heat, Lap, Racer
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class RacerInline(admin.StackedInline):
    model = Racer
    can_delete = False
    verbose_name_plural = 'racers'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Heat)
admin.site.register(Lap)
admin.site.register(Racer)
