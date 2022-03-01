from django.contrib import admin

from .models import Blog, Blogger, Comment


# Register your models here.
class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'last_name', 'first_name', 'date_of_birth']
    list_filter = ['nickname', 'last_name', 'date_of_birth']
    inlines = [BlogInline]


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'blogger', 'pub_date']
    list_filter = ['title', 'blogger', 'pub_date']
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'blogger', 'pub_date']
    list_filter = ['blog', 'blogger', 'pub_date']