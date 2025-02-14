from django.contrib import admin
from .models import*


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
        'description',
        'time_create',
        'category',
        'status',
        'is_complete'
        ]
    prepopulated_fields ={
        'slug': ['name'],
    }
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'