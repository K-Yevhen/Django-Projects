# blog/models.py
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_models/', null=True, blank=True)
    slug = models.SlugField(max_length=50, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
