import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser



def user_directory_path(instance, filename):
    return f'user_{instance.id}/profile_pictures/{filename}'


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    telegram_id = models.BigIntegerField(unique=True, blank=True, null=True)
    telegram_confirmation_code = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username
    
    
    def generate_random_string(self, length=10, chars=string.ascii_letters + string.digits):
        """Генерирует случайную строку заданной длины"""
        return ''.join(random.choices(chars, k=length))
    
    def generate_confirmation_code(self):
        """Метод для генерации уникального кода подтверждения."""
        code = self.generate_random_string()
        while CustomUser.objects.filter(telegram_confirmation_code=code).exists():
            code = self.generate_random_string()
        return code
        
    def save(self, *args, **kwargs):
        if not self.telegram_confirmation_code:
            self.telegram_confirmation_code = self.generate_confirmation_code()
        super().save(*args, **kwargs)
        