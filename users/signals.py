"""User app signal handler."""
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_profile.models import UserProfile
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_profile(_, instance, created, **kwargs):
    """Create an object of UserProfile when a user CustomUser object is created."""
    if created:
        UserProfile.objects.create(user=instance)
