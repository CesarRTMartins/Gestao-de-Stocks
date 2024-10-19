from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_Products, name='list_Products'),  # URL para a lista de produtos
    path('add/', views.add_product, name='add_product'),  # URL para adicionar produtos
]
