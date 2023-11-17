"""User Profile Forms."""
from django import forms

from . import models

ACCOUNT_CHOICES = ((1, "Student"), (2, "Teacher"))


class UserProfileCreateForm(forms.ModelForm):
    """User profile create view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES)

    class Meta:
        """Meta class."""

        model = models.UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture"]


class UserProfileUpdateForm(forms.ModelForm):
    """User profile change view."""

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

    class Meta:
        """Meta class."""

        model = models.UserProfile
        fields = ["first_name", "last_name", "gender", "age", "picture"]
