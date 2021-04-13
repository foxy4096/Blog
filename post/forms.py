from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('slug', 'author')
        widgets = {
                'content': forms.Textarea(attrs={
                'style': 'height: 200px;width:500px'}),
                }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
                'body': forms.Textarea(attrs={
                'style': 'height: 200px;width:500px'}),
                }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']