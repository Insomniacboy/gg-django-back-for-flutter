from django.db import models

from django.contrib.auth import get_user_model
import random

class Info(models.Model):
    body = models.TextField()
    """ price = models.TextField() """
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    """user = "Client"
    password = "Qtv]&K4kk@s(Y7qz"  """

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']