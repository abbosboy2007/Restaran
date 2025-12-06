from django import forms
from .models import Chefs

class ChefsForm(forms.ModelForm):
    class Meta:
        model = Chefs
        fields = ['name', 'bio', 'image']