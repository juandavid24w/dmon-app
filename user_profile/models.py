"""User profile model."""
from django.db import models


class UserProfile(models.Model):
    """UserProfile model class."""

    class Gender(models.IntegerChoices):
        """Gender choice class."""

        FEMALE = 1
        MALE = 2
        OTHER = 3

    custom_user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    gender = models.IntegerField(choices=Gender.choices, default=Gender.FEMALE)
    age = models.IntegerField(default=1)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
