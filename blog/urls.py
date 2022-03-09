from django.urls import path, re_path

from . import views

app_name = 'blog'
urlpatterns = [
    path('index', views.index, name='index'),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^comments/$', views.CommentListView.as_view(), name='comments'),
    re_path(r'^blogger/create/$', views.BloggerCreate.as_view(), name='blogger_create'),
    re_path(r'^blogger/(?P<pk>\d+)/update/$', views.BloggerUpdate.as_view(), name='blogger_update'),
    re_path(r'^blogger/(?P<pk>\d+)/delete/$', views.BloggerDelete.as_view(), name='blogger_delete'),
    re_path(r'^blog/create/$', views.BlogCreate.as_view(), name='blog_create'),
    re_path(r'^blog/(?P<pk>\d+)/update/$', views.BlogUpdate.as_view(), name='blog_update'),
    re_path(r'^blog/(?P<pk>\d+)/delete/$', views.BlogDelete.as_view(), name='blog_delete'),
    re_path(r'^comment/create/$', views.CommentCreate.as_view(), name='comment_create'),
    re_path(r'^comment/(?P<pk>\d+)/update/$', views.CommentUpdate.as_view(), name='comment_update'),
    re_path(r'^comment/(?P<pk>\d+)/delete/$', views.CommentDelete.as_view(), name='comment_delete'),
]
