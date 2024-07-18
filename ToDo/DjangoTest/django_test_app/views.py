from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm, Registration, Login
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
from .mixins import IsUserAuth


class HomePage(IsUserAuth, ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'


class RegistrationPage(CreateView):
    template_name = 'registration.html'
    # fields = ['username', ]
    # model = User
    form_class = Registration
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_list.html'
    success_url = reverse_lazy('home')

    @method_decorator(csrf_exempt)
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
    success_url = reverse_lazy('home')

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'id': self.object.id}, status=200)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = Login
    redirect_authenticated_user = True
