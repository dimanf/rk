# -*- coding: utf-8 -*-
from django.contrib import admin
from rk.first_task.models import Table5

class Table5Admin(admin.ModelAdmin):
	list_display = ('id', 'date', 'ip1', 'ip2', 'byte')
	list_display_links = ('id',)
	search_fields = ('date',)
	ordering = ('date',)

admin.site.register(Table5, Table5Admin)