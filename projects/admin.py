# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Location, Project, SubProject, ServiceType


class LocationAdmin(admin.ModelAdmin):
	list_display = ('location', 'region')


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'start_time', 'end_time')


class SubProjectAdmin(admin.ModelAdmin):
	list_display = ('name',)


class SerciceTypeAdmin(admin.ModelAdmin):
	list_display = ('service_type',)



admin.site.register(Location, LocationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(SubProject, SubProjectAdmin)
admin.site.register(ServiceType, SerciceTypeAdmin)
