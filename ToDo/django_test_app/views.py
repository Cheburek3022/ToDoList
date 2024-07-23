from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm, Login, UserRegisterForm, AuthenticationForm
from .models import User, Task
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .mixins import IsUserAuth


class HomePage(IsUserAuth, ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_list.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        task_data = {
            'id': self.object.id,
            'title': self.object.title,
            'deadline': self.object.deadline.strftime('%Y-%m-%d')
        }
        return JsonResponse({'task': task_data}, status=200)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'id': self.object.id}, status=200)


class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class TaskUpdateView(IsUserAuth, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'updatetask.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')
