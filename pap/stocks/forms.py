# stocks/forms.py
from django import forms
from .models import Products, StockProduct
from .models import ProductCategory
from .models import Movements
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category','reference','name',]  # Inclua os campos que deseja no formulário

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']  # Inclua os campos desejados

class DeleteProductForm(forms.Form):
    id = forms.ChoiceField(
        label="Select Product to Delete",
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super(DeleteProductForm, self).__init__(*args, **kwargs)
        # Atualiza as opções dinamicamente com os produtos disponíveis
        self.fields['id'].choices = [(product.id, product.name) for product in Products.objects.all()]

class DeleteCategoryForm(forms.Form):
    id = forms.ChoiceField(
        label="Select Category to Delete",
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super(DeleteCategoryForm, self).__init__(*args, **kwargs)
        # Atualiza as opções dinamicamente com as categorias disponíveis
        self.fields['id'].choices = [(category.id, category.name) for category in ProductCategory.objects.all()]

class MovementForm(forms.ModelForm):
    ACTION_CHOICES = [
        ('entry', 'Entry'),  # Entrada de estoque
        ('exit', 'Exit'),    # Saída de estoque
    ]

    action = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Movements
        fields = ['quantity']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']