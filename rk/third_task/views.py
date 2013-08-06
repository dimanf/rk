# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext

def third_task(request):
    
    return render(request, 'third_task/third_task.html')

def json_list(request):    
    return render_to_response('third_task/json_list.json',
    	mimetype='application/json; charset=UTF-8',
    	context_instance = RequestContext(request))
