from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', name='blogs'),
    path('blogger/<author-id>', name='author'),
    path('<blog-id>', name='blog'),
    path('bloggers/', name='bloggers'),
    path('<blog-id>/create', name='create'),

]