"""Forms for accounts app."""
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Registration form."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ("email",)


class TeacherSignUpForm(UserCreationForm):
    """Sign up form for Teachers."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        """Overwrite default method."""
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    """Sign up form for Students."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        """Overwrite default method."""
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user
