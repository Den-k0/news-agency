from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
class TopicListView(generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_form.html"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_form.html"


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")
    template_name = "newspaper/topic_confirm_delete.html"
