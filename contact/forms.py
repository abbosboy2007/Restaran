from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'discription']
        # widgets = {
        #     'topic': forms.TextInput(attrs={'placeholder': 'Subject'}),
        #     'discription': forms.Textarea(attrs={'placeholder': 'Description'}),
        # }