from django.http import  HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def main_view(requests):
    return render(requests, 'views/main.html')

@login_required
def home_view(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'views/home.html', {'posts': posts})

    
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'views/post_detail.html',{'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'views/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'views/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        post.delete()
        return redirect('post-detail')
    return render(request, 'views/post_confirm_delete.html', {'post': post})
