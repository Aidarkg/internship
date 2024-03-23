from django.contrib import admin
from aidar.models import Task


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    list_display_links = ('id', 'title', 'completed')
    
    