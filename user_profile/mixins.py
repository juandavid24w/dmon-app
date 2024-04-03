"""User role Mixins."""

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserProfileRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """User Profile Object Required Mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is student.

        Returns
        -------
        bool
            True, when there is a `UserProfile` object for the current user.
            False, otherwise.

        """
        # When test_func is directly called by some function, handle not logged in users here
        if self.request.user.is_anonymous:
            return False

        userprofile = self.request.user.userprofile
        return userprofile.is_student or userprofile.is_teacher

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("user_profile:profile_update")


class StudentRequiredMixin(UserProfileRequiredMixin, UserPassesTestMixin):
    """Student role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is student.

        Returns
        -------
        bool
            True, when current user is student.
            False, otherwise.

        """
        return super().test_func() and self.request.user.userprofile.is_student

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        # if parent mixin's test_func fails, call its handle_no_permission instead of handling here
        if not super().test_func():
            return super().handle_no_permission()

        redirect_url = reverse_lazy("polls:question-list")
        return redirect(redirect_url)


class TeacherRequiredMixin(UserProfileRequiredMixin, UserPassesTestMixin):
    """Teacher role required mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is teacher.

        Returns
        -------
        bool
            True, when current user is student.
            False, otherwise.

        """
        return super().test_func() and self.request.user.userprofile.is_teacher

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        # if parent mixin's test_func fails, call its handle_no_permission instead of handling here
        if not super().test_func():
            return super().handle_no_permission()

        redirect_url = reverse_lazy("polls:question-list")
        return redirect(redirect_url)
