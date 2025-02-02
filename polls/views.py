"""
This module contains views for the polls application.
Functions:
    index(request): Display the latest questions.
    detail(request, question_id): Display the details of a specific question.
    results(request, question_id): Display the results of a specific question.
    vote(request, question_id): Vote for a specific question.
"""

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    """
    Display the latest questions.
    """

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by(
            "-pub_date"
        )[:5]
        # __lte is less than or equal to
        # __gt is greater than
        # __lt is less than
        # __gte is greater than or equal to
        # __exact is equal to
        # __iexact is case-insensitive equal to
        # __contains is contains
        # __icontains is case-insensitive contains
        # __in is in
        # __startswith is starts with
        # __istartswith is case-insensitive starts with
        # __endswith is ends with
        # __iendswith is case-insensitive ends with
        # __range is in range
        # __year is year
        # __month is month
        # __day is day
        # __week_day is week day
        # __hour is hour
        # __minute is minute
        # __second is second
        # __isnull is null
        # __search is search
        # __regex is regex
        # __iregex is case-insensitive regex


class DetailView(generic.DetailView):
    """
    Display the details of a specific question, while ensuring that the future question is not published.
    """

    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """
    Display the results of a specific question.
    """

    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    """
    Vote for a specific question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
