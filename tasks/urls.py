from django.urls import path

from .views import *

app_name = "tasks"
urlpatterns = [
    path('all_tasks/', AllTasks.as_view(), name='all_tasks'),
    path('task/<slug:slug>/', SingleTask.as_view(), name='single_task'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('edit_task/<slug:slug>/', EditTask.as_view(), name='edit_task'),
    path('delete_task/<slug:slug>/', DeleteTask.as_view(), name='delete_task'),
    # path('complete_task/<int:pk>/', complete_task, name='complete_task'),
]
