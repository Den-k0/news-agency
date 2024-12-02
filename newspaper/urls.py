from django.urls import path
from newspaper.views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("topic/create", TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/update", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/<int:pk>/delete", TopicDeleteView.as_view(), name="topic-delete"),
]

app_name = "newspaper"
