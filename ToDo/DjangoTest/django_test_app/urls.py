from django.urls import path
from . import views
from .views import HomePage, TaskCreateView, TaskDeleteView


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('tasks/add/', TaskCreateView.as_view(), name='add_task'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path("registration/", views.RegistrationPage.as_view(), name="registration"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.LoginPage.as_view(), name="login")
]



