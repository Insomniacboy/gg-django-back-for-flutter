from enum import unique
from turtle import position
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models

class Info(models.Model):
    """"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    position_id = models.IntegerField()
    buy_or_sell = models.BooleanField()

    """def __str__(self):
        return self.title_ru[0:50]"""

    class Meta:
        ordering = ['-updated']

class SubInfo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(Info, related_name='subcategories', on_delete=models.CASCADE)
    title = models.TextField()
    position_id = models.IntegerField()
    buy_or_sell = models.BooleanField()

    class Meta:
        unique_together = ['subcategory', 'position_id']
        ordering = ['position_id']

    def __str__(self):
        return '%d: %s' % (self.position_id, self.title)
