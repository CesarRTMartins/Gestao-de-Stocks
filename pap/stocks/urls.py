from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_Products, name='list_Products'),  # URL para a lista de produtos
    path('ListCategories/', views.list_categories, name='List_Categories'),  # Exemplo para a lista
    path('AddCategory/', views.add_category, name='Add_Category'),
    path('AddProduct/', views.add_product, name='Add_Product'),  # URL para adicionar produtos
]
    