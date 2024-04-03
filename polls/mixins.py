"""User role Mixins."""

from django.shortcuts import redirect
from django.urls import reverse_lazy

from user_profile.mixins import TeacherRequiredMixin


class TeacherAuthorRequiredMixin(TeacherRequiredMixin):
    """Teacher role and author of the `Question` object required mixin."""

    def dispatch(self, request, *args, **kwargs):
        """Redirect if the object is not owned by the current user."""
        # if TeacherRequiredMixin's test_func does not pass, call its handle_no_permission to handle
        if not super().test_func():
            return super().handle_no_permission()

        obj = self.get_object()

        redirect_url = reverse_lazy("polls:question-detail", kwargs={"pk": obj.id})

        if obj.author != self.request.user:
            return redirect(redirect_url)

        return super().dispatch(request, *args, **kwargs)
