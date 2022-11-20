"""Accounts app URL Configuration."""
from django.urls import path
from django.views.generic import TemplateView

from users import views

app_name = "users"
urlpatterns = [
    path("", TemplateView.as_view(template_name="registration/signup.html"), name="signup"),
    path("signup/student/", views.StudentSignUpView.as_view(), name="student_signup"),
    path("signup/teacher/", views.TeacherSignUpView.as_view(), name="teacher_signup"),
]
