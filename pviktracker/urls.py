from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^heats(/(?P<year>\d{4})(/(?P<month>\d{1,2})(/(?P<day>\d{1,2})/(?P<number>\d{1,3})?)?)?)?', 'tracker.views.heats', name='heats')
)
