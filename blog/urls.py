from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^comments/$', views.CommentListView.as_view(), name='comments'),
    re_path(r'^blogger/create/$', views.BloggerCreate.as_view(), name='blogger_create'),
    re_path(r'^blogger/(?P<pk>\d+)/update/$', views.BloggerUpdate.as_view(), name='blogger_update'),
    re_path(r'^blogger/(?P<pk>\d+)/delete/$', views.BloggerDelete.as_view(), name='blogger-delete'),

    #re_path(r'^comment/(?P<pk>\d+)$', views.CommentDetailView.as_view(), name='comment-detail'),
    #path('<blog-id>/create', name='create'),
]