from django import forms
from .models import Category, Manls

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title',]

class ManlsForm(forms.ModelForm):
    class Meta:
        model = Manls
        fields = ['category', 'image', 'name', 'description', 'price']