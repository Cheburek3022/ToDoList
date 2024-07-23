from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=300, blank=True)


class Task(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Login(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=18)