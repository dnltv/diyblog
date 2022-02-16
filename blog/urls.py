from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^comment/(?P<pk>\d+)$', views.CommentDetailView.as_view(), name='comment-detail'),
    re_path(r'^comments/$', views.CommentListView.as_view(), name='comments'),
    #path('<blog-id>/create', name='create'),
]