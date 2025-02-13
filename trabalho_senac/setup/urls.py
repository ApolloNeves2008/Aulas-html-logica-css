"""
URL configuration for setup project.

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
from django.urls import path

#Aqui informamaos quais funções temos na views
from livros.views import sobre, fun_section, fun_home, delete_section, senhor, indicacao, catalogo, emprestimo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre, name='sobre'),
    path('indicacao/', indicacao, name='indicacao'),
    path('catalogo/', catalogo, name='catalogo'),
     path('emprestimo/', emprestimo, name='emprestimo'),
    path('', fun_section, name='sessao'),
    path('home/', fun_home, name='inicio'),
    path('delete_section/', delete_section, name="delete_section"),
    path('senhor/', senhor, name="senhor")
]