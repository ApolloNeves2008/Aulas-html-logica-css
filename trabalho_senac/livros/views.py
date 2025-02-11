from django.shortcuts import render
from .models import livro

# importa o modelo do livro

from .models import livro

#Função que rendereiza a pagina html com os dados dos alunos

def alugar(request):
  return render(request, "alugar.html")

def catalogo(request):
   return render(request, "cadastroDeLivros.html")

def home(request):
   return render(request, "home.html")

def login(request):
   return render(request, "login.html")

