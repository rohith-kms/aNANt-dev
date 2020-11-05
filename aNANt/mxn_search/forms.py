from django import forms

class SearchForm(forms.Form):

    M1 = forms.CharField(max_length=3,required=False)
    M2 = forms.CharField(max_length=3,required=False)
    X  = forms.CharField(max_length=3,required=False)
    T1 = forms.CharField(max_length=3,required=False)
    T2 = forms.CharField(max_length=3,required=False)
