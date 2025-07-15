from django.contrib import admin
from .models import Task, SubTask


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1  # количество пустых форм


class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask)
