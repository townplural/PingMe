from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'telegram_id', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'telegram_id']
    ordering = ['id',]
    