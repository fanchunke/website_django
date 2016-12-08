# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from projects.models import Project

# The ArticleType Model
class ArticleType(models.Model):
	article_type = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name_plural = "文章类型"


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

	class Meta:
		verbose_name_plural = "文章"

	
	def __unicode__(self):
		return self.title