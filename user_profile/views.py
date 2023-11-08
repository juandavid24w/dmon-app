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
    template_name = "user_profile/userprofile_detail.html"
    slug_field = None
    slug_url_kwarg = ""

    def get_object(self, queryset: list = None):
        """Owner of the object should be the current user."""
        return self.model.objects.filter(custom_user=self.request.user).first()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Profile update view."""

    model = UserProfile
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy("user_profile:profile_detail")
    template_name = "generic_create_update_form.html"
    extra_context = {"title_text": "Edit Profile", "button_text": "Update"}

    def get_object(self, queryset: list = None):
        """Owner of the object should be the current user."""
        return self.model.objects.filter(custom_user=self.request.user).first()

    def get_context_data(self, **kwargs):
        """Set the current value of first_name and last_name in the form from the current user."""
        context = super().get_context_data(**kwargs)
        account_type = 1 if self.request.user.userprofile.is_student else 2
        context["form"] = UserProfileUpdateForm(
            instance=self.request.user.userprofile,
            initial={
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
                "account_type": account_type,
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
        account_type = int(form.cleaned_data["account_type"])
        if account_type == 1:
            profile.is_student, profile.is_teacher = True, False
        else:
            profile.is_student, profile.is_teacher = False, True
        profile.save()
        user.save()
        return super().form_valid(form)
