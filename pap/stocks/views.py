from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Products, ProductCategory, StockProduct, StockHistory # Importa o modelo que você criou para itens no estoque
from django.http import HttpResponse
from .forms import ProductForm
from .forms import *
from .forms import ProductCategoryForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserCreationForm
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
        # Obtém o ID do produto enviado pelo formulário
        product_id = request.POST.get('product')  
        if product_id:
            # Obtém o objeto Produto ou retorna 404
            product = get_object_or_404(Products, id=product_id)
            
            # Deleta o produto
            product.delete()
            
            # Adiciona mensagem de sucesso
            messages.success(request, f"The product '{product.name}' has been deleted successfully!")
            return redirect('list_Products')  # Redireciona para a lista de produtos
        else:
            # Adiciona mensagem de erro se nenhum produto foi selecionado
            messages.error(request, "No product selected for deletion.")
    
    # Obtém todos os produtos para exibir no dropdown
    products = Products.objects.all()

    # Renderiza a página com a lista de produtos
    return render(request, 'stocks/delete_product.html', {'products': products})

def delete_category(request):
    if request.method == 'POST':
        # Obtém o ID da categoria enviada pelo formulário
        category_id = request.POST.get('category')
        if category_id:
            # Obtém o objeto Categoria ou retorna 404
            category = get_object_or_404(ProductCategory, id=category_id)

            # Deleta a categoria
            category.delete()

            # Adiciona mensagem de sucesso
            messages.success(request, f"The category '{category.name}' has been deleted successfully!")
            return redirect('List_Categories')  # Redireciona para a lista de categorias
        else:
            # Adiciona mensagem de erro se nenhuma categoria for selecionada
            messages.error(request, "No category selected for deletion.")

    # Obtém todas as categorias para exibir no dropdown
    categories = ProductCategory.objects.all()

    # Renderiza a página com a lista de categorias
    return render(request, 'stocks/delete_category.html', {'categories': categories})

def manage_stock(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    stock = StockProduct.objects.filter(product=product).first()

    if request.method == 'POST':
        action = request.POST.get('action')  # 'add' ou 'remove'
        quantity = int(request.POST.get('quantity', 0))
        price = request.POST.get('price', None)

        if action == 'add':
            stock, created = StockProduct.objects.get_or_create(product=product)
            stock.quantity += quantity
            stock.price = price  # Atualiza o preço do produto
            stock.save()

            StockHistory.objects.create(product=product, change_type='add', quantity_changed=quantity, price=price)

        elif action == 'remove':
            if stock and stock.quantity >= quantity:
                stock.quantity -= quantity
                stock.save()

                StockHistory.objects.create(product=product, change_type='remove', quantity_changed=quantity)

        return redirect('list_Products')

    # Se for um GET, renderiza o template
    return render(request, 'stocks/manage_stock.html', {'product': product, 'stock': stock})

def stock_history(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    history = StockHistory.objects.filter(product=product).order_by('-timestamp')

    return render(request, 'stocks/stock_history.html', {'product': product, 'history': history})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login/")  # Redireciona para login após registo bem-sucedido
    else:
        form = UserCreationForm()
    
    return render(request, "stocks/register.html", {"form": form})


