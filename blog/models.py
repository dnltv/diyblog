from datetime import datetime
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Blogger(models.Model):
    """
    Model representating a blogger.
    """
    first_name = models.CharField(max_length=100, help_text='Enter your name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name', null=True, blank=True)
    nickname = models.CharField(max_length=100, help_text='Enter your nickname',)
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, help_text="Tell something about yourself")

    def get_absolute_url(self):
        """
        Returns url to access a particular blogger instance
        """
        return reverse('blog:blogger-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']


class Like(models.Model):
    """
    Model representating a Like.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Blog(models.Model):
    """
    Model representating a Blog
    """
    title = models.CharField(max_length=100, help_text='Enter the title of the blog', default='Untitled')
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, help_text='Enter some text')
    pub_date = models.DateTimeField(default=datetime.now())
    likes = GenericRelation(Like)

    def get_absolute_url(self):
        """
        Returns url to access a particular blog instance.
        """
        return reverse('blog:blog-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title}'

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-pub_date']
        permissions = (('can_post_blog', 'Post a blog'), ('can_delete_blog', 'Delete a blog'),)


class Comment(models.Model):
    """
    Model representating a Comment.
    """
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, help_text='Add a comment')
    pub_date = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        """
        Reverse to accept a particular instance of comment.
        """
        return reverse('blog:comment-detail', args=[str(self.id)])

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['pub_date']








