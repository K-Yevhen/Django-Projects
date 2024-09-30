from django.contrib import admin
from .models import Author, Category, BlogPost

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(BlogPost)
