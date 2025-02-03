from django.shortcuts import render
from .models import Alunos
# Create your views here.
def alunos_list(request):
  
    #Conecta com a base de dados que criamas e tras todos os alunos cadastrados.
 
 
 #Aqui a função retorna a pagina alunos_list.html 
 #A pasta cadastro deverá ser criada dentro da pasta templates
 #O arquivo alunos_lsit.html deve ser criada dentro da pasta cadastro
  return render(request, "alunos_list.html")

def alunos_contato(request):
  return render(request, "alunos_contato.html")

