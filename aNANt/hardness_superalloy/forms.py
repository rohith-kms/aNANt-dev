from django import forms
from .models import Image


class HardnessForm(forms.ModelForm):

    Al = forms.DecimalField(max_value=100,min_value=0)
    Co = forms.DecimalField(max_value=100,min_value=0)
    Nb = forms.DecimalField(max_value=100,min_value=0)
    W = forms.DecimalField(max_value=100,min_value=0)
    Re = forms.DecimalField(max_value=100,min_value=0)
    C = forms.DecimalField(max_value=100,min_value=0)
    B = forms.DecimalField(max_value=100,min_value=0)
    P = forms.DecimalField(max_value=100,min_value=0)
    S = forms.DecimalField(max_value=100,min_value=0)

    Mo = forms.DecimalField(max_value=100,min_value=0)
    Hf = forms.DecimalField(max_value=100,min_value=0)
    Ta = forms.DecimalField(max_value=100,min_value=0)
    Cu = forms.DecimalField(max_value=100,min_value=0)
    Si = forms.DecimalField(max_value=100,min_value=0)


    Ti = forms.DecimalField(max_value=100,min_value=0)
    V = forms.DecimalField(max_value=100,min_value=0)
    Cr = forms.DecimalField(max_value=100,min_value=0)
    Mn = forms.DecimalField(max_value=100,min_value=0)
    Fe = forms.DecimalField(max_value=100,min_value=0)
    Ni = forms.DecimalField(max_value=100,min_value=0)
    Zr = forms.DecimalField(max_value=100,min_value=0)
    ann_time = forms.DecimalField(max_value=200,min_value=0)
    ann_temp = forms.DecimalField(max_value=2000,min_value=0)
    
    class Meta:
        model = Image
        fields=('imagefile',)         
#image = forms.ImageField(max_length=500)
