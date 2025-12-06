from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'email', 'date', 'guests', 'time', 'special_requests']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            
        }