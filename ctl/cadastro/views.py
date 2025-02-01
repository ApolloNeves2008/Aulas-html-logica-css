from django.shortcuts import render
from .models import Alunos
# Create your views here.
def alunos_list(request):
   return render(request, 'cadastro/alunos_list.html')

def alunos_contato(request):
 return render(request, 'cadastro/alunos_contato.html')
