# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rk.first_task.views import Table5List
from rk.third_task.views import json_list
from rk.third_task.views import third_task

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^first_task/$', Table5List.as_view()),
    url(r'^third_task/$', third_task),
    url(r'^json_list/$', json_list),
    # url(r'^$', 'rk.views.home', name='home'),
    # url(r'^rk/', include('rk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
