from django.db import models

# Create your models here.

class Mxene(models.Model):

    # name of the mxene

    name = models.CharField(max_length=15)

    # these are the elements of the mxene

    M1 = models.CharField(max_length=3)
    M2 = models.CharField(max_length=3)
    X  = models.CharField(max_length=3)
    T1 = models.CharField(max_length=3)
    T2 = models.CharField(max_length=3)

    # Some important properties

    Lc = models.FloatField(null=True)    # Lattice constant
    Bg = models.FloatField(null=True)    # Band gap
    Mm = models.FloatField(null=True)    # Magnetic moment


    #Ph = models.CharField(max_length=10)     # Phase


    #--- files. all imformation about the MXene is contained in these

    # beta version files

    poscar_file = models.FileField(upload_to='poscars')
    bands_image = models.ImageField(upload_to='images')

    #struct_file         = models.FileField() # contains structure data
    #band_struct_file    = models.FileField() # contains bans structure data
    #props_file          = models.FileField() # contains table of properties
    #dos_file            = models.FileField() # contains density of states data
    #misc_file           = models.FileField() # contains misc info like Author,date

    # return name when called in console

    def __str__(self):
        return self.name
