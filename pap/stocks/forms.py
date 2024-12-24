# stocks/forms.py
from django import forms
from .models import Products
from .models import ProductCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category','reference','name', 'description', 'price','weight','img','quantity',]  # Inclua os campos que deseja no formulário

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']  # Inclua os campos desejados
