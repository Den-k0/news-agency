from django.urls import path

from accounts.views import (
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    RedactorListView,
)

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
    NewspaperDetailView,
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
    path('new/<int:pk>/', NewspaperDetailView.as_view(), name='newspaper-detail'),

    # Redactor
    path("redactor/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactor/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactor/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
]

app_name = "newspaper"
