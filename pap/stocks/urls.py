from django.urls import path
from . import views
from . views import export_products_csv


urlpatterns = [
    path('', views.list_Products, name='list_Products'),  # URL para a lista de produtos
    path('ListCategories/', views.list_categories, name='List_Categories'),  # Exemplo para a lista
    path('AddCategory/', views.add_category, name='Add_Category'),
    path('AddProduct/', views.add_product, name='Add_Product'),  # URL para adicionar produtos
    path('DeleteProduct/', views.delete_product, name='Delete_Product'),
    path('DeleteCategory/', views.delete_category, name='Delete_Category'),
    path('stocks/manage/<int:product_id>/', views.manage_stock, name='manage_stock'),
    path('stock/history/<int:product_id>/', views.stock_history, name='stock_history'),
    path('export/csv/',export_products_csv, name='export_csv'),
]