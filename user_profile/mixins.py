"""User role Mixins."""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
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
        x = False

        try:
            x = self.request.user.userprofile
        except ObjectDoesNotExist:
            x = False

        return x

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("user_profile:profile_create")


class UserProfileNotCreatedRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """User Profile Object Not Created Required Mixin."""

    def test_func(self) -> bool:
        """Overriding `test_func` to check if the current logged in user is student.

        Returns
        -------
        bool
            True, when there is a `UserProfile` object for the current user.
            False, otherwise.

        """
        x = True

        try:
            x = self.request.user.userprofile
        except ObjectDoesNotExist:
            x = True

        return not x

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        return redirect("user_profile:profile_detail")


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
        return self.request.user.userprofile.is_student

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
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
        return self.request.user.userprofile.is_teacher

    def handle_no_permission(self):
        """Handle no permission error, redirect to some other pages."""
        redirect_url = reverse_lazy("polls:question-list")
        return redirect(redirect_url)
