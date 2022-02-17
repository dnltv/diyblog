from django import forms
from django.core.exceptions import *
from django.utils.translation import gettext_lazy as _
import datetime


class BlogForm(forms.Form):

    title = forms.CharField(help_text="Enter a title of blog.")
    text = forms.CharField(help_text='Enter a text.')

