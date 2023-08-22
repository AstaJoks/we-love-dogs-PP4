from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    """
    Form class to add a post
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')


class EditPostForm(forms.ModelForm):
    """
    Form class to edit a post
    """

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
