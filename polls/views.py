"""
This module contains views for the polls application.
Functions:
    index(request): Display the latest questions.
    detail(request, question_id): Display the details of a specific question.
    results(request, question_id): Display the results of a specific question.
    vote(request, question_id): Vote for a specific question.
"""

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    """
    Display the latest questions.
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """
    Display the details of a specific question.
    """
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """
    Display the results of a specific question.
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """
    Vote for a specific question.
    """
    return HttpResponse(f"Youre voting on {question_id}.")
