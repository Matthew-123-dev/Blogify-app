from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(config_name='blog_post'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter your post title...'
        })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']