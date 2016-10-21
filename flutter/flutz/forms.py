from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Post, Member


class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['flutt', 'flutter_user']
