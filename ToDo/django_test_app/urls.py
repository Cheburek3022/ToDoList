from django.urls import path
from . import views
# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePage, TaskCreateView, TaskDeleteView, UserRegisterView, UserLoginView, TaskUpdateView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('tasks/add/', TaskCreateView.as_view(), name='add_task'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('registration/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]



