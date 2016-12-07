from django.contrib import admin
from .models import Project, ArticleType, Article, ServiceType, Location, SubProject

# Register your models here.
admin.site.register(Project)
admin.site.register(ArticleType)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'project', 'article_type', 'pub_time', 'mod_time')
	# readonly_fields = ("pub_time","mod_time",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ServiceType)
admin.site.register(Location)
admin.site.register(SubProject)
