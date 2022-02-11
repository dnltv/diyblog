from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'blogs/$', views.BloggerListView.as_view(), name='blogs'),
    path(r'^blogger/(?P<pk>\d+)$', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path(r'blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    path(r'^bloggers/$', views.BloggerListView.as_view(), name='bloggers'),
    #path('<blog-id>/create', name='create'),
]