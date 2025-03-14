# Generated by Django 5.1.6 on 2025-03-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_category_options_alter_status_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-time_create', 'is_complete'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
