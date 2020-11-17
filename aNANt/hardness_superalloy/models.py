from django.db import models



# Create your models here.


class Image(models.Model):
    imagefile = models.FileField(upload_to='vicker-images/')

    def __str__(self):
        return str(self.imagefile)
