from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # ... (Keep existing fields) ...
    # Add related_name='posts' if not already there, though not strictly necessary for this step
    pass 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
