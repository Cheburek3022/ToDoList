import django.contrib.auth.mixins
from django.shortcuts import render, redirect


class IsUserAuth(django.contrib.auth.mixins.AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")
        return super().dispatch(request, *args, **kwargs)