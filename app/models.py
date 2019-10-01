"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Teststatus(models.Model):
    username=models.ForeignKey( User,
          on_delete=models.CASCADE,)
    taken_test = True

