from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Redactor
from newspaper.forms import TopicSearchForm, NewspaperSearchForm
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
    queryset = Topic.objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset


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
    queryset = Newspaper.objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(title__icontains=form.cleaned_data["title"])
        return self.queryset

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
