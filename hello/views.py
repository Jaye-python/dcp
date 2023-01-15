from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")

from django.utils import timezone
from django.views.generic.list import ListView

from .models import Person

class ArticleListView(ListView):

    model = Person
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
