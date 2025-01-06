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

class DeleteProductForm(forms.Form):
    id = forms.ChoiceField(
        label="Select Product to Delete",
        choices=[],
    )

    def __init__(self, *args, **kwargs):
        super(DeleteProductForm, self).__init__(*args, **kwargs)
        # Atualiza as opções dinamicamente com os produtos disponíveis
        self.fields['id'].choices = [(product.id, product.name) for product in Products.objects.all()]

