from django.shortcuts import render
from .models import Alunos
# Create your views here.
#Função que rendereiza a pagina html com os dados dos alunos
 #Aqui a função retorna a pagina alunos_list.html 
 #A pasta cadastro deverá ser criada dentro da pasta templates
 #O arquivo alunos_lsit.html deve ser criada dentro da pasta cadastro
def alunos_list(request):
    dados_alunos = Alunos.objects.all()
    return render(request, 'alunos_list.html', {'dados': dados_alunos})