# BLOGLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from django.db import models


class Post(models.Model):
    """
    We make a model to store posts.
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    body = models.TextField(max_length=50000)
    date = models.DateTimeField(auto_now=True)