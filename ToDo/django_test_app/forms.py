from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task, User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline']


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'email', "password1", "password2"]

class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
