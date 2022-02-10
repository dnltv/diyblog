from django.db import models
from django.urls import reverse


# Create your models here.
class Blogger(models.Model):
    """
    Model representating a blogger.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=500)

    def get_absolute_url(self):
        """
        Returns url to access a particular blogger instance
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'



#class Blog(models.Model):
    #"""
    #Model representating a Blog
    #"""
