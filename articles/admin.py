# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Article, ArticleType


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'project', 'article_type', 'pub_time', 'mod_time')


class ArticleTypeAdmin(admin.ModelAdmin):
	list_display = ('article_type', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)