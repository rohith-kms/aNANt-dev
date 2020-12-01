from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone

# Model for a post made by user

class Post(models.Model):

    title = models.CharField(max_length=100)    # Title of the post
    text = models.CharField(max_length=500)		# Content
    author = models.CharField(max_length=30)	# Username of poster
    created_date = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True)	# Whether this post is public or not

class Comment(models.Model):

    post = models.ForeignKey('forum.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)		# Content
    author = models.CharField(max_length=30)	# Username of commenter
    created_date = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True)	# Whether this post is public or not
