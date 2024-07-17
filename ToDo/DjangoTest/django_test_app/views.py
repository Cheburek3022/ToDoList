from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import User, Task
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class HomePage(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        task_data = {
            'id': self.object.id,
            'title': self.object.title,
            'deadline': self.object.deadline.strftime('%Y-%m-%d')
        }
        return JsonResponse({'task': task_data}, status=200)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'id': self.object.id}, status=200)