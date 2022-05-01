from django.db import models

class Info(models.Model):
    """"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title_ru = models.TextField()
    desc_ru = models.TextField()
    title_en = models.TextField()
    desc_en = models.TextField()
    title_kg = models.TextField()
    desc_kg = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    address = models.TextField()
    instagram = models.TextField()
    facebook = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    zoom = models.TextField()
    gallery_id = models.TextField()
    

    """def __str__(self):
        return self.title_ru[0:50]"""

    class Meta:
        ordering = ['-updated']