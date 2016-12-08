# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# The locations where the project locates.
class Location(models.Model):
	location = models.CharField(max_length=50, unique=True)
	region = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "落地"


	def __unicode__(self):
		return self.location


# The service types which project belongs to.
class ServiceType(models.Model):
	service_type = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name_plural = "服务类型"


	def __unicode__(self):
		return self.service_type


# the subprojects of project
class SubProject(models.Model):
	name = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name_plural = "子项目"
			
	def __unicode__(self):
		return self.name


# The Project Model.
class Project(models.Model):
	name = models.CharField(max_length=100)
	introduction = models.TextField()	
	start_time = models.DateField()
	end_time = models.DateField()
	subprojects = models.ManyToManyField(SubProject, related_name='projects')
	service_types = models.ManyToManyField(ServiceType, related_name='projects')
	locations = models.ManyToManyField(Location, related_name='projects')

	class Meta:
		verbose_name_plural = "项目"


	def __unicode__(self):
		return self.name
