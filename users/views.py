"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic

from users.forms import StudentSignUpForm, TeacherSignUpForm


class StudentSignUpView(generic.CreateView):
    """Sign up view for Student Users."""

    form_class = StudentSignUpForm
    template_name = "registration/signup_form.html"
    success_url = reverse_lazy("login")
    extra_context = {"user_type": "Student"}


class TeacherSignUpView(generic.CreateView):
    """Sign up view for Teacher Users."""

    form_class = TeacherSignUpForm
    template_name = "registration/signup_form.html"
    success_url = reverse_lazy("login")
    extra_context = {"user_type": "Teacher"}
