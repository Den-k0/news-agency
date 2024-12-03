from django.urls import path
from newspaper.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    # Topic
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("topic/create", TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/update", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/<int:pk>/delete", TopicDeleteView.as_view(), name="topic-delete"),

    # Newspaper
    path("newspaper/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspaper/create", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/update", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspaper/<int:pk>/delete", NewspaperDeleteView.as_view(), name="newspaper-delete"),
]

app_name = "newspaper"
