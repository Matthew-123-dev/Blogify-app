from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'content'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']