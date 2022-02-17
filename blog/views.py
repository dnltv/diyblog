from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blogger, Blog, Comment


# Create your views here.
def index(request):
    """
    Index page view function.
    """
    text = "That's my new project index page!"
    num_of_bloggers = Blogger.objects.count()
    num_of_blogs = Blog.objects.count()
    num_of_comments = Comment.objects.count()
    return render(request,
                  'index.html',
                  context={
                      'text': text,
                      'num_of_bloggers': num_of_bloggers,
                      'num_of_blogs': num_of_blogs,
                      'num_of_comments': num_of_comments,
    })


class BloggerDetailView(DetailView):
    model = Blogger


class BloggerListView(ListView):
    model = Blogger
    paginate_by = 10


class BlogDetailView(DetailView):
    model = Blog


class BlogListView(ListView):
    model = Blog
    paginate_by = 10


class CommentDetailView(DetailView):
    model = Comment


class CommentListView(ListView):
    model = Comment
    paginate_by = 10


class BloggerCreate(CreateView):
    model = Blogger
    fields = '__all__'


class BloggerUpdate(UpdateView):
    model = Blogger
    fields = ['first_name', 'last_name', 'nickname', 'date_of_birth', 'description']


class BloggerDelete(DeleteView):
    model = Blogger
    success_url = reverse_lazy('blog:bloggers')


class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'text']


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blogs')


class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text']


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog:comments')


