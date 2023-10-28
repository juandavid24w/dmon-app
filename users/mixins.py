"""User role Mixins."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


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
        return self.request.user.is_student

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
        return self.request.user.is_teacher

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("polls:question-list")
