from django.urls import path
from . import views
from .views import HomePage, TaskCreateView, TaskDeleteView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('tasks/add/', TaskCreateView.as_view(), name='add_task'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
]

