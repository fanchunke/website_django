from django.contrib import admin
from .models import Project, ArticleType, Article

# Register your models here.
admin.site.register(Project)
admin.site.register(ArticleType)
admin.site.register(Article)
