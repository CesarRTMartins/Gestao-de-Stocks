# stocks/forms.py
from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'quantity']  # Inclua os campos que deseja no formulário