from django.db import models

# Create your models here.

class Materials(models.Model) :

    # name of the mxene

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name