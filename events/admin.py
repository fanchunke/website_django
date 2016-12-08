# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'location', 'project', 'subproject', 'nums', 'time')


admin.site.register(Event, EventAdmin)