"""User Profile Forms."""
from django import forms

from user_profile.models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = ("name", "gender", "age", "picture")
