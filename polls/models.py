"""Polls models."""
from datetime import timedelta

from django.db import models
from django.utils.timezone import now

from users.models import CustomUser


class Question(models.Model):
    """Question model class.

    Attributes:
    ----------
    author : ForeignKey
        Holds the author of the question.
    answered_by : ManyToManyField
        Holds the users who have answered the question.
    question_text : string
        Holds the text for the question.
    pub_date : datetime
        Holds the date and time of the question.

    """

    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    answered_by = models.ManyToManyField(CustomUser, related_name="question_users")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        """Return a string representation of Question."""
        return str(self.question_text)

    def was_published_recently(self):
        """Check if Question was published in last 24 hours.

        Returns:
        -------
        bool:
            True, if published in last 24 hours.
            False, otherwise.

        """
        return now() >= self.pub_date >= now() - timedelta(days=1)


class Choice(models.Model):
    """Choice model class.

    Attributes:
    ----------
    answered_choice : ManyToManyField
        Holds the users who have answered the question with the choice.
    question : foreign key
        Holds a reference to the Question class object.
    choice_text : string
        Holds a string that represents a choice.

    """

    answered_choice = models.ManyToManyField(CustomUser, related_name="choice_users")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        """Return a string representation of Choice."""
        return str(self.choice_text)
