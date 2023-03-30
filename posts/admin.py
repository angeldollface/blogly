# BLOGLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from django.contrib import admin
from .models import Post

# We make the "Post" model
# available to the admins.
admin.site.register(Post)
