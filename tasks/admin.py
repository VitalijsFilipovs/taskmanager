from django.contrib import admin
from .models import Task, SubTask

# Инлайн-форма подзадач внутри задач
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

# Кастомное отображение задач с инлайн подзадачами и коротким заголовком
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'status', 'deadline')
    inlines = [SubTaskInline]

    def short_title(self, obj):
        return obj.title if len(obj.title) <= 10 else obj.title[:10] + '...'
    short_title.short_description = 'Title'

# Кастомный admin action для перевода подзадач в статус "Done"
@admin.action(description="Отметить выбранные подзадачи как Done")
def mark_subtasks_done(modeladmin, request, queryset):
    queryset.update(status='Done')

# Админка для подзадач с action'ом и основными полями
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'task')
    actions = [mark_subtasks_done]