from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
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


#class CommentUpdate(LoginRequiredMixin, UpdateView):
    #model = Comment
    #form = ComemntForm
    #login_url = '/login/'
    #redirect_field_name = 'redirect_to'
    #template_name =
    #context_name =


#class smth(PermissionRequiredMixin, smthView):
    #permission_required = 'blog.can_post_blog'
    #permission_required = ('can_post_blog', 'Post a blog')