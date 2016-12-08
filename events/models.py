# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from projects.models import Location, Project, SubProject

# the event of project
class Event(models.Model):
	title = models.CharField(max_length=50, verbose_name='标题')
	time = models.DateTimeField(verbose_name='时间')
	nums = models.IntegerField(verbose_name='参与人数')
	project = models.ForeignKey(Project, related_name='events',verbose_name='项目')
	subproject = models.ForeignKey(SubProject, related_name='events', verbose_name='子项目')
	location = models.ForeignKey(Location, related_name='events', verbose_name='落地')

	class Meta:
		verbose_name_plural = "活动"


	def __unicode__(self):
		return self.title