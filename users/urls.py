"""Accounts app URL Configuration."""
from django.urls import path
from django.views.generic import TemplateView

from users import views

app_name = "users"
urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
]
