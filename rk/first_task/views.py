# -*- coding: utf-8 -*-
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from rk.first_task.models import Table5
from django.views.generic import ListView

class Table5List(ListView):
	model = Table5	
	queryset = Table5.objects.values('ip1', 'ip2',).annotate(sum_bytes=Sum('byte')).order_by('-date')
