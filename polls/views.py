"""Polls app views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views import View, generic

# Local imports
from polls.models import Choice, Question
from users.mixins import StudentRequiredMixin, TeacherRequiredMixin


class CreateQuestionView(TeacherRequiredMixin, generic.CreateView):
    """View to create question."""

    model = Question
    fields = ["question_text"]
    success_url = reverse_lazy("polls:index")

    def form_valid(self, form: object) -> object:
        """For valid form submission.

        - Set the published date as the current date and time.
        - Set the author as the current logged in user.

        """
        form.instance.pub_date = now()
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreateChoiceView(TeacherRequiredMixin, generic.CreateView):
    """View to create choice."""

    model = Choice
    fields = ["choice_text"]

    def get_success_url(self) -> object:
        """Overwrite the `success_url`."""
        question_id = self.kwargs["pk"]
        return reverse_lazy("polls:detail", kwargs={"pk": question_id})

    def form_valid(self, form: object) -> object:
        """If the form data is valid, add current time as `pub_date`."""
        form.instance.question_id = self.kwargs["pk"]
        return super().form_valid(form)


class IndexView(generic.ListView):
    """Index view of polls app."""

    model = Question
    queryset = Question.objects.order_by("-pub_date")[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """Detail view of polls app."""

    model = Question


class ResultsView(LoginRequiredMixin, generic.DetailView):
    """Results view of polls app."""

    model = Question
    template_name = "polls/results.html"


class SubmitVote(StudentRequiredMixin, View):
    """Vote View."""

    def post(self, request: object, question_id: int) -> object:
        """Vote counter function.

        - Set the `answered_by` for the `question` and `choice` objects as the current user.
        - Increment the `votes` for the `choice` by one.

        """
        question = get_object_or_404(Question, pk=question_id)
        try:
            question.answered_by.add(self.request.user)
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
            selected_choice.answered_choice.add(self.request.user)
            selected_choice.votes += 1
            selected_choice.save()
            question.save()
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                "polls/details.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
