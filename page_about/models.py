from django.db import models

class Info(models.Model):
    """"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title_ru = models.TextField()
    title_text_ru = models.TextField()
    title_en = models.TextField()
    title_text_en = models.TextField()
    title_kg = models.TextField()
    title_text_kg = models.TextField()

    """def __str__(self):
        return self.title_ru[0:50]"""

    def __str__(self):
        return self.title_ru[0:50]

    def __str__(self):
        return self.title_text_ru[0:50]

    def __str__(self):
        return self.title_en[0:50]

    def __str__(self):
        return self.title_text_en[0:50]

    def __str__(self):
        return self.title_kg[0:50]

    def __str__(self):
        return self.title_text_kg[0:50]

    class Meta:
        ordering = ['-updated']