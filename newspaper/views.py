from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from accounts.forms import RedactorCreationForm, RedactorUpdateForm
from accounts.models import Redactor
from newspaper.models import Newspaper, Topic


def index(request):
    number_of_redactors = Redactor.objects.count()
    number_of_news = Newspaper.objects.count()
    context = {
        "number_of_redactors": number_of_redactors,
        "number_of_news": number_of_news,
    }
    return render(request, "newspaper/index.html", context=context)


# Topic
class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"
    paginate_by = 5


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_confirm_delete.html"


# Newspaper
class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 3


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_form.html"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_form.html"


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_confirm_delete.html"


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
