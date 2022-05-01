from django.db import models

class Info(models.Model):
    """"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    number = models.TextField()
    smscode = models.TextField()

    """def __str__(self):
        return self.title_ru[0:50]"""

    class Meta:
        ordering = ['-updated']