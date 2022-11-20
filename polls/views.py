"""Polls app views."""
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views import View, generic
from django.views.generic.edit import CreateView

# Local imports
from polls.models import Choice, Question
from users.mixins import StudentRequiredMixin, TeacherRequiredMixin


class CreateQuestionView(TeacherRequiredMixin, CreateView):
    """View to create question."""

    model = Question
    fields = ["question_text"]
    success_url = reverse_lazy("polls:index")

    def form_valid(self, form):
        """For valid form submission."""
        form.instance.pub_date = now()
        return super().form_valid(form)


class CreateChoiceView(TeacherRequiredMixin, CreateView):
    """View to create choice."""

    login_url = settings.LOGIN_URL
    redirect_field_name = "redirect_to"
    model = Choice
    fields = ["choice_text"]

    def get_success_url(self):
        """Overwrite the `success_url`."""
        question_id = self.kwargs["pk"]
        return reverse_lazy("polls:detail", kwargs={"pk": question_id})

    def form_valid(self, form):
        """If the form data is valid, add current time as `pub_date`."""
        form.instance.question_id = self.kwargs["pk"]
        return super().form_valid(form)


class IndexView(generic.ListView):
    """Index view of polls app."""

    model = Question

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """Detail view of polls app."""

    model = Question


class ResultsView(LoginRequiredMixin, generic.DetailView):
    """Results view of polls app."""

    model = Question
    template_name = "polls/results.html"


class SubmitVote(StudentRequiredMixin, View):
    """Vote View."""

    def post(self, request, question_id):
        """Vote counter function."""
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                "polls/details.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
