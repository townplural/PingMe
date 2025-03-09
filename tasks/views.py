from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import get_page_title


class AllTasks(LoginRequiredMixin, ListView):
    
    """
    шаблон есть
    Остались только косметические правки всякие
    Просмотр всех задач 
    Так же можно отметить выполнение задачи (Галочка)
    Обновить статус задачи(Не начата, В процессе, Завершена)
    
    """
    
    model = Task
    template_name = 'tasks/all_tasks.html'
    paginate_by = 10
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = get_page_title('all_tasks')
        return context
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-time_create')
    
    


class SingleTask(LoginRequiredMixin, DetailView):
    
    """
    
    шаблон есть
    Просмотр атрибутов отдельной задачи:
    Название, описание, сроки и т.д.
    
    """
    
    model = Task
    template_name = 'tasks/single_task.html'
    context_object_name = 'task'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = get_page_title('single_task')
        return context
    


class CreateTask(LoginRequiredMixin, CreateView):
    
    """
    Есть форма для отпраки задачи в БД
    Остались только косметические правки
    Создание задачи:
    Название, описание, сроки и т.д.
    
    """
    
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = get_page_title('create_task')
        return context
    
    def get_success_url(self):
        return reverse('tasks:single_task', kwargs={'slug': self.object.slug})

    
    


class EditTask(LoginRequiredMixin, UpdateView):
    
    """
    шаблона нет
    Изменение задачи:
    Названия, описания, сроков и т.д.
    Так же есть возможность удаления задачи 
    При изменении задачи будет перенаправление на просмотр отдельно задачи
    SingleTask(DetailView)
    
    """
    
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = get_page_title('edit_task')
        return context
    
    def get_success_url(self):
        return reverse('tasks:single_task', kwargs={'slug': self.object.slug})
    


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name ='tasks/delete_task.html'
    
    def get_success_url(self):
        return reverse('tasks:all_tasks')
        


def complete_task(request, pk): 
    tasks = Task.objects.filter(is_complete=True)
    return HttpResponse('')


