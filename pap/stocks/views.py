from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Products, ProductCategory, StockProduct # Importa o modelo que você criou para itens no estoque
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

def edit_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    categories = ProductCategory.objects.all()

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")

        # Atualizar a categoria
        category_id = request.POST.get("category")
        if category_id:
            product.category = get_object_or_404(ProductCategory, id=category_id)

        # Atualizar quantidade de stock no modelo Products
        stock_quantity = request.POST.get("quantity")

        if stock_quantity:
            stock_quantity = int(stock_quantity)
            product.quantity = stock_quantity  # Atualiza o campo principal do produto

            # Verifica se já existe um registro no StockProduct para este produto
            stock_entry = StockProduct.objects.filter(product=product).order_by('-entry_date').first()

            if stock_entry:       
                # Atualiza o registro mais recente ao invés de criar um novo
                stock_entry.quantity = stock_quantity
                stock_entry.entry_date = timezone.now()
                stock_entry.save()
            else:
                # Caso não exista, cria um novo registro
                StockProduct.objects.create(product=product, quantity=stock_quantity, entry_date=timezone.now())

        product.save()
        return redirect('list_Products')

    return render(request, 'stocks/edit_product.html', {'product': product, 'categories': categories})
