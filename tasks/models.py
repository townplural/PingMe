from django.db import models
# from django.utils.text import slugify (Не поддерживает русский язык)
from pytils.translit import slugify # Поддерживает русский язык
from user.models import CustomUser


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            n = 1
            while Task.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{n}"
                n+=1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ["-time_create", "is_complete"]
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Status(models.Model):

    
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
