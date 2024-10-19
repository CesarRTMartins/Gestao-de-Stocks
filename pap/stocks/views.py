from django.shortcuts import render, redirect
from .models import Products # Importa o modelo que você criou para itens no estoque
from django.http import HttpResponse
from .forms import ProductForm
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
