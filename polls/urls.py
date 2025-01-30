"""
URL configuration for the polls app.
This module defines the URL patterns for the polls application. It includes
routes for the index view, detail view, results view, and vote action.
Routes:
    - "" (index): Displays the index view of the polls.
    - "<int:pk>/" (detail): Displays the detail view of a specific poll.
    - "<int:pk>/results/" (results): Displays the results view of a specific poll.
    - "<int:question_id>/vote/" (vote): Handles voting for a specific poll.
Attributes:
    app_name (str): The name of the application namespace.
    urlpatterns (list): A list of URL patterns for the polls app.

"""

from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
