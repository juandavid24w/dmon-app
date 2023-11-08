"""User role Mixins."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Student role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is student.

        Returns:
        -------
        bool
            True, when current user is student.
            False, otherwise.

        """
        return self.request.user.userprofile.is_student

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("polls:question-list")


class TeacherRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Teacher role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is teacher.

        Returns:
        -------
        bool
            True, when current user is student.
            False, otherwise.

        """
        return self.request.user.userprofile.is_teacher

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("polls:question-list")


class TeacherAuthorRequiredMixin(TeacherRequiredMixin, UserPassesTestMixin):
    """Teacher role and author of object required mixin."""

    def dispatch(self, request, *args, **kwargs):
        """Redirect if the object is not owned by the current user."""
        obj = self.get_object()

        if obj.author != self.request.user:
            return redirect(
                reverse_lazy("polls:question-detail", kwargs={"pk": obj.id})
            )

        return super().dispatch(request, *args, **kwargs)
