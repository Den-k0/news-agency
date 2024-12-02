from django.shortcuts import render

from accounts.models import Redactor
from newspaper.models import Newspaper


def index(request):
    number_of_redactors = Redactor.objects.count()
    number_of_news = Newspaper.objects.count()
    context = {
        "number_of_redactors": number_of_redactors,
        "number_of_news": number_of_news,
    }
    return render(request, "newspaper/index.html", context=context)
