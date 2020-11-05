from django.db import models

# Create your models here.

# all the apps go here.

class AnantApp(models.Model):

    name = models.CharField(max_length=25) # name of the ANANT app
    app_url = models.CharField(max_length=15) # url corresponding to app

    app_image = models.ImageField(upload_to='media/app_images')

    def __str__(self):
        return self.name
