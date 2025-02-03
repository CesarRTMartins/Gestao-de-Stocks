from django.urls import path
from . import views
from .views import edit_product


urlpatterns = [
    path('', views.list_Products, name='list_Products'),  # URL para a lista de produtos
    path('ListCategories/', views.list_categories, name='List_Categories'),  # Exemplo para a lista
    path('AddCategory/', views.add_category, name='Add_Category'),
    path('AddProduct/', views.add_product, name='Add_Product'),  # URL para adicionar produtos
    path('DeleteProduct/', views.delete_product, name='Delete_Product'),
    path('DeleteCategory/', views.delete_category, name='Delete_Category'),
    path('EditProduct/<int:product_id>/', edit_product, name='edit_product'),
]