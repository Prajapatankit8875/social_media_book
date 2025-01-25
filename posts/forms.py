from .models import Post
from django import forms


class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","image","caption")

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('body',)
