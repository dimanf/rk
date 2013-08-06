# -*- coding: utf-8 -*-
from django.db import models

class Table5(models.Model):
	date = models.DateField()
	time = models.TimeField()
	ip1 = models.CharField(max_length=15)
	ip2 = models.CharField(max_length=15)
	byte = models.IntegerField()

	def __unicode__(self):
		return '%s' % self.id