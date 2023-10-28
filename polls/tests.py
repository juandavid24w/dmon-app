"""Tests for polls app."""
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from django.utils.timezone import now
from parameterized import parameterized

from polls.models import Choice, Question


class QuestionModelTest(TestCase):
    """Test for Question model."""

    @classmethod
    def setUpTestData(cls):
        """Set up method."""
        Question.objects.create(question_text="test question", pub_date=now())

    def test_question_text_field_value(self):
        """Test question text field value."""
        question = Question.objects.create(question_text="Question 1", pub_date=now())
        self.assertEqual("Question 1", question.question_text)

    @parameterized.expand(
        [
            (now() + timedelta(days=30), False),
            (now() - timedelta(days=1, seconds=1), False),
            (now() - timedelta(hours=23, minutes=59), True),
        ]
    )
    def test_was_published_recently(self, input_date, expected):
        """Test `was_published_recently` function."""
        question = Question(pub_date=input_date)
        self.assertEqual(question.was_published_recently(), expected)


class ChoiceModelTest(TestCase):
    """Test for `Choice` Model."""

    @classmethod
    def setUpTestData(cls):
        """Set up method."""
        question = Question.objects.create(question_text="test question", pub_date=now())
        Choice.objects.create(question=question, choice_text="choice 1")
        Choice.objects.create(question=question, choice_text="choice 2", votes=3000)

    def test_choice_test_field_value(self):
        """Test choice_text field value."""
        choice = Choice.objects.get(id=1)
        self.assertEqual("choice 1", choice.choice_text)

    def test_choice_votes_value(self):
        """Test `votes` field of choice."""
        choice1 = Choice.objects.get(id=1)
        choice2 = Choice.objects.get(id=2)
        self.assertEqual(0, choice1.votes)
        self.assertEqual(3000, choice2.votes)


class QuestionIndexViewTests(TestCase):
    """Test IndexView."""

    def test_no_questions(self):
        """Test No question text displayed when no object in Model."""
        response = self.client.get(reverse("polls:question-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["object_list"], [])
