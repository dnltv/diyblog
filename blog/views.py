from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from .models import Blogger


# Create your views here.
def index(request):
    """
    Index page view function.
    """
    text = "That's my new project index page!"
    return render(request,
                  'index.html',
                  context={
                      'text': text,
    })


class BloggerDetailView(DetailView):
    model = Blogger


class BloggerListView(ListView):
    model = Blogger
    paginate_by = 20