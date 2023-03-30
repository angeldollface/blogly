# BLOGLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from .models import Post
from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/home.html', context)


def post(request, pk):
    post = Post.objects.get(pk=pk)
    title = post.title
    description = post.description
    body = post.body
    date = post.date
    context = {
        'title': title,
        'date': date,
        'description': description,
        'body': body
    }
    return render(request, 'posts/post.html', context)
