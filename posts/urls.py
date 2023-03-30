# BLOGLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from .views import post
from .views import post_list
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='home'),
    path('posts/<int:pk>/', post, name='post'),
]