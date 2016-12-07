# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# The locations where the project locates.
class Location(models.Model):
	location = models.CharField(max_length=50, unique=True)
	region = models.CharField(max_length=50)

	def __unicode__(self):
		return self.location


# The service types which project belongs to.
class ServiceType(models.Model):
	service_type = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.service_type


# the subprojects of project
class SubProject(models.Model):
	name = models.CharField(max_length=50, unique=True)

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

	def __unicode__(self):
		return self.name


# The ArticleType Model
class ArticleType(models.Model):
	article_type = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.article_type


# The Article Model.
class Article(models.Model):
	title = models.CharField(max_length=100, verbose_name='标题')
	body = models.TextField()	
	pub_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
	mod_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
	article_type = models.ForeignKey(ArticleType, related_name='articles', verbose_name='分类')
	project = models.ForeignKey(Project, related_name='articles', verbose_name='项目')

	def __unicode__(self):
		return self.title


# the event of project
class Event(models.Model):
	title = models.CharField(max_length=50)
	time = models.DateTimeField()
	nums = models.IntegerField()
	project = models.ForeignKey(Project, related_name='events')
	subproject = models.ForeignKey(SubProject, related_name='events')
	location = models.ForeignKey(Location, related_name='events')