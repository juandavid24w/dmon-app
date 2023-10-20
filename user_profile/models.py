"""User profile model."""
from django.db import models


class UserProfile(models.Model):
    """UserProfile model class."""

    class Gender(models.IntegerChoices):
        """Gender choice class."""

        FEMALE = 1
        MALE = 2
        OTHERS = 3

    custom_user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    gender = models.IntegerField(choices=Gender.choices, default=Gender.OTHERS)
    age = models.IntegerField(default=69)
    picture = models.ImageField(upload_to="profile_pictures/", blank=True)
