"""
Definition of models.
"""

from django.db import models


class Post(models.Model):
        post_heading = models.CharField(max_length=200)
        post_text = models.TextField()
        def __str__(self): # If python2 use __str__ if python3
            return unicode(self.user)
# Create your models here.
