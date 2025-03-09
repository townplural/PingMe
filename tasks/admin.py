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
    



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    
