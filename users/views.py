"""Accounts view."""
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm
from users.models import CustomUser


class StudentSignUpView(generic.CreateView):
    """Sign up view for Student Users."""

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("login")
    extra_context = {"title_text": "Student Sign Up", "button_text": "Register"}

    def form_valid(self, form):
        """For valid form submission."""
        form.instance.is_student = True
        return super().form_valid(form)


class TeacherSignUpView(generic.CreateView):
    """Sign up view for Teacher Users."""

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "generic_create_update_form.html"
    success_url = reverse_lazy("login")
    extra_context = {"title_text": "Teacher Sign Up", "button_text": "Register"}

    def form_valid(self, form):
        """For valid form submission."""
        form.instance.is_teacher = True
        return super().form_valid(form)
