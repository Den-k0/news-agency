from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import RedactorCreationForm, RedactorUpdateForm
from accounts.models import Redactor


# Redactor
class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 5


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
