"""Polls app URL."""
from django.urls import path

from polls import views

app_name = "polls"

urlpatterns = [
    path("question/add/", views.CreateQuestionView.as_view(), name="create-question"),
    path("<int:pk>/choice/add/", views.CreateChoiceView.as_view(), name="create-choice"),
    path("", views.QuestionListView.as_view(), name="question-list"),
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="question-detail"),
    path("<int:pk>/edit/", views.UpdateQuestionView.as_view(), name="update-question"),
    path("<int:pk>/delete/", views.DeleteQuestionView.as_view(), name="delete-question"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.SubmitVote.as_view(), name="vote"),
]
