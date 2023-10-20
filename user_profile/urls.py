"""User profile app URL."""
from django.urls import path

from user_profile import views as profile_views

app_name = "user_profile"

urlpatterns = [
    path("profile/", profile_views.UserProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/", profile_views.UserProfileUpdateView.as_view(), name="profile_update"),
]
