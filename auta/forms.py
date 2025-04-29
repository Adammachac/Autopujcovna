from django import forms
from .models import Zakaznik

class ZakaznikForm(forms.ModelForm):
    class Meta:
        model = Zakaznik
        fields = ['jmeno', 'prijmeni']
