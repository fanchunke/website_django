# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from projects.models import Location, Project, SubProject

# the event of project
class Event(models.Model):
	title = models.CharField(max_length=50)
	time = models.DateTimeField()
	nums = models.IntegerField()
	project = models.ForeignKey(Project, related_name='events')
	subproject = models.ForeignKey(SubProject, related_name='events')
	location = models.ForeignKey(Location, related_name='events')

	class Meta:
		verbose_name_plural = "活动"


	def __unicode__(self):
		return self.title