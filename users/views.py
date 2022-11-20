"""Accounts view."""
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import StudentSignUpForm, TeacherSignUpForm
from users.models import CustomUser


class StudentSignUpView(CreateView):
    """Sign up view for Student Users."""

    model = CustomUser
    form_class = StudentSignUpForm
    template_name = "registration/signup_form.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        """Set the `user_type` as "student" in the form data."""
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)


class TeacherSignUpView(CreateView):
    """Sign up view for Teacher Users."""

    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = "registration/signup_form.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        """Set the `user_type` as "student" in the form data."""
        kwargs["user_type"] = "teacher"
        return super().get_context_data(**kwargs)
