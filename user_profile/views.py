"""User profile view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from user_profile.forms import UserProfileUpdateForm
from user_profile.models import UserProfile


# Create your views here.
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """Profile detail view.

    Reason why `slug_field` and `slug_url_kwargs` are set as `None`:
    - By default, in a `DetailView`, the object of the model is retrieved from the URL parameters.
    - In this case, as the model is `UserProfile`, the object of user is retrieved from the request.

    """

    model = UserProfile
    template_name = "user_profile/profile.html"
    slug_field = None
    slug_url_kwarg = ""

    def get_object(self, queryset: list = None):
        """Owner of the object should be the current user."""
        return self.model.objects.filter(custom_user=self.request.user).first()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view."""

    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = "user_profile/profile_update.html"
    success_url = reverse_lazy("user_profile:profile_detail")

    def get_object(self, queryset: list = None):
        """Owner of the object should be the current user."""
        return self.model.objects.filter(custom_user=self.request.user).first()

    def get_context_data(self, **kwargs):
        """Set the current value of first_name and last_name in the form from the current user."""
        context = super().get_context_data(**kwargs)
        context["form"] = UserProfileUpdateForm(
            instance=self.request.user.userprofile,
            initial={
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
            },
        )
        return context

    def form_valid(self, form: object):
        """Set custom_user Field of the current object as the current user."""
        profile = form.save(commit=False)
        profile.custom_user = self.request.user
        user = self.request.user
        user.last_name = form.cleaned_data["last_name"]
        user.first_name = form.cleaned_data["first_name"]
        profile.save()
        user.save()
        return super().form_valid(form)
