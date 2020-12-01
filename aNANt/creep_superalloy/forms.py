from django import forms

class CreepForm(forms.Form):

    Al = forms.DecimalField(max_value=100,min_value=0)
    Co = forms.DecimalField(max_value=100,min_value=0)
    Nb = forms.DecimalField(max_value=100,min_value=0)
    Mo = forms.DecimalField(max_value=100,min_value=0)
    Hf = forms.DecimalField(max_value=100,min_value=0)
    Ta = forms.DecimalField(max_value=100,min_value=0)
    W = forms.DecimalField(max_value=100,min_value=0)
    B = forms.DecimalField(max_value=100,min_value=0)
    Ru = forms.DecimalField(max_value=100,min_value=0)
    ann_temp1 = forms.DecimalField(max_value=2000,min_value=0)
    ann_time1 = forms.DecimalField(max_value=500,min_value=0)
    ann_temp2 = forms.DecimalField(max_value=2000,min_value=0)
    ann_time2 = forms.DecimalField(max_value=500,min_value=0)


    Ti = forms.DecimalField(max_value=100,min_value=0)
    V = forms.DecimalField(max_value=100,min_value=0)
    Cr = forms.DecimalField(max_value=100,min_value=0,)
    Mn = forms.DecimalField(max_value=100,min_value=0,)
    Fe = forms.DecimalField(max_value=100,min_value=0,)
    Ni = forms.DecimalField(max_value=100,min_value=0,)
    Cu = forms.DecimalField(max_value=100,min_value=0,)
    Zn = forms.DecimalField(max_value=100,min_value=0,)
    Zr = forms.DecimalField(max_value=100,min_value=0,)
    Rh = forms.DecimalField(max_value=100,min_value=0,)
    Re = forms.DecimalField(max_value=100,min_value=0,)
    C  = forms.DecimalField(max_value=100,min_value=0,)
    Si = forms.DecimalField(max_value=100,min_value=0,)
    P  = forms.DecimalField(max_value=100,min_value=0,)
    S  = forms.DecimalField(max_value=100,min_value=0,)
    N  = forms.DecimalField(max_value=100,min_value=0,)
    

    thermal_cond = forms.DecimalField(min_value=0)
    stress = forms.DecimalField(min_value=0)
    temperature = forms.DecimalField(max_value=2000,min_value=0)

