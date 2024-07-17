from django.apps import AppConfig


class DjangoTestAppConfig(AppConfig):
    default_auto_field = 'ToDo.db.models.BigAutoField'
    name = 'django_test_app'
