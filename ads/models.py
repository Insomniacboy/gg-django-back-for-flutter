from uuid import uuid4
from django.db import models
import os 


class Info(models.Model):
    """"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    desc = models.TextField()
    price = models.TextField()
    phone = models.TextField()
    category_id = models.TextField()
    region_id = models.TextField()
    published = models.BooleanField()

    """def __str__(self):
        return self.title_ru[0:50]"""

    class Meta:
        ordering = ['-updated']



def path_and_rename(instance, filename):
    upload_to = 'ads_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Image(models.Model):
    information = models.ForeignKey(Info, on_delete=models.CASCADE)
    # url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=path_and_rename)
    
    """
    def cache(self):
        if self.url and not self.image:
            result = urllib.urlretrieve(self.url)
            self.image.save(
                os.path.basename(self.url),
                File(open(result[0], 'rb'))
            )
        self.save()
        """