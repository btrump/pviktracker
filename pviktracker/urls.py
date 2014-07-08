from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tracker.views.home', name='home'),
    url(r'^heats/?$', 'tracker.views.heat_list', name='heat_list'),
    url(r'^heats/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<heat>\d{1,3})/?', 'tracker.views.heat_detail', name='heat_detail'),
)
