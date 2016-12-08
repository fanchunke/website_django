# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# The locations where the project locates.
class Location(models.Model):
	location = models.CharField(max_length=50, unique=True, verbose_name='落地居委')
	region = models.CharField(max_length=50, verbose_name='所属街道')

	class Meta:
		verbose_name_plural = "落地"


	def __unicode__(self):
		return self.location


# The service types which project belongs to.
class ServiceType(models.Model):
	service_type = models.CharField(max_length=50, unique=True, verbose_name='服务类型')
	introduction = models.CharField(max_length=100, default='暂无简介', verbose_name='简介')

	class Meta:
		verbose_name_plural = "服务类型"


	def __unicode__(self):
		return self.service_type


# the subprojects of project
class SubProject(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name='子项目')
	introduction = models.CharField(max_length=100, default='暂无简介', verbose_name='简介')

	class Meta:
		verbose_name_plural = "子项目"
			
	def __unicode__(self):
		return self.name


# The Project Model.
class Project(models.Model):
	name = models.CharField(max_length=100, verbose_name='项目')
	introduction = models.TextField(verbose_name='简介')	
	start_time = models.DateField(verbose_name='起始时间')
	end_time = models.DateField(verbose_name='结项时间')
	subprojects = models.ManyToManyField(SubProject, related_name='projects', verbose_name='子项目')
	service_types = models.ManyToManyField(ServiceType, related_name='projects', verbose_name='服务类型')
	locations = models.ManyToManyField(Location, related_name='projects', verbose_name='落地')

	class Meta:
		verbose_name_plural = "项目"


	def __unicode__(self):
		return self.name
