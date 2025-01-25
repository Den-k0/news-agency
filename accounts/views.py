from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import RedactorCreationForm, RedactorUpdateForm, RedactorSearchForm
from accounts.models import Redactor


# Redactor
class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = RedactorSearchForm(self.request.GET)
        if search_form.is_valid():
            name = search_form.cleaned_data.get("name")
            if name:
                queryset = queryset.filter(
                    Q(first_name__icontains=name) | Q(last_name__icontains=name)
                )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all()
    template_name = "newspaper/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
    form_class = RedactorCreationForm
    template_name = "newspaper/redactor_form.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
    template_name = "newspaper/redactor_confirm_delete.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
    form_class = RedactorUpdateForm
    template_name = "newspaper/redactor_form.html"
