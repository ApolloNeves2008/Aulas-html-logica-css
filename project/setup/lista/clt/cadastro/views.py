from django.shortcuts import render

from cadastro.models import Aluno

# Create your views here.
def home(request):
    return render(request, "base.html")

def alunos(request):
    return render(request, "cadastrados.html")

def contato(request):
    return render(request, "contato.html")

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request,'listar_alunos.html', {'alunos': alunos})