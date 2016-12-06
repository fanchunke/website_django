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


# The Project Model.
class Project(models.Model):
	name = models.CharField(max_length=100)
	service_type = models.ManyToManyField(ServiceType, related_name='projects')
	introduction = models.TextField()
	locations = models.ManyToManyField(Location, related_name='projects')
	start_time = models.DateField()
	end_time = models.DateField()

	def __unicode__(self):
		return self.name


# the article type
class ArticleType(models.Model):
	article_type = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.article_type


# The Article Model.
class Article(models.Model):
	title = models.CharField(max_length=100)
	pub_time = models.DateTimeField(auto_now_add=True)
	mod_time = models.DateTimeField(auto_now=True)
	body = models.TextField()
	article_type = models.ForeignKey(ArticleType, related_name='articles')
	project = models.ForeignKey(Project, related_name='articles')

	def __unicode__(self):
		return self.title


