from django.shortcuts import render, redirect
from .models import Products, ProductCategory # Importa o modelo que você criou para itens no estoque
from django.http import HttpResponse
from .forms import ProductForm
from .forms import *
from .forms import ProductCategoryForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Home Page! This is your default view.")

def list_Products(request):
    products = Products.objects.all()  # Vai buscar todos os produtos á base de dados
    return render(request, 'stocks/Products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Gurada o produto no banco de dados
            return redirect('list_Products')  # Redireciona para a página de lista de produtos após salvar
    else:
        form = ProductForm()
    return render(request, 'stocks/add_product.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('List_Categories')  # Substitua por sua URL de lista de categorias
    else:
        form = ProductCategoryForm()
    return render(request, 'stocks/add_category.html', {'form': form})

def list_categories(request):
    categories = ProductCategory.objects.all()
    return render(request, 'stocks/Categories.html', {'categories': categories})

def delete_product(request):
    if request.method == 'POST':
        form = DeleteProductForm(request.POST)
        if form.is_valid():
            # Obtém o ID do produto do formulário
            product_id = form.cleaned_data['id']
            
            # Obtém o objeto Produto ou retorna 404
            product = get_object_or_404(Products, id=product_id)
            
            # Deleta o produto
            product.delete()
            
            # Adiciona mensagem de sucesso
            messages.success(request, f"The product '{product.name}' has been deleted successfully!")
            return redirect('list_Products')  # Redireciona para a lista de produtos
    else:
        form = DeleteProductForm()

    # Renderiza o formulário para exclusão
    return render(request, 'stocks/delete_product.html', {'form': form})
