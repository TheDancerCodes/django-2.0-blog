"""Add Blog Model to the administration site."""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
