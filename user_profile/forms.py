"""User Profile Forms."""
from django import forms

from user_profile.models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture"]
