"""
URL configuration for pap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stocks import views  # Importa as views do app stocks
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from stocks.views import register  # Importa as views do app stocks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', include('stocks.urls')),
    # Redireciona a raiz para o login
    path('', lambda request: redirect('login/'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='stocks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register/", register, name="register"),
]
