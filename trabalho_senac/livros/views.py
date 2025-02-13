from django.shortcuts import render, redirect
from .models import livro

# importa o modelo do livro

from .models import livro

#Função que rendereiza a pagina html com os dados dos alunos

def fun_home(request):
    return render(request, "livros\catalogo.html")

def alugar(request):
  return render(request, "livros\emprestar.html")
 
def senhor(request):
   return render(request, "inspecao\senhor.html")

def sobre(request):
    return render(request, "livros\sobre.html")

def indicacao(request):
    return render(request, "livros\indicacao.html")

def catalogo(request):
    return render(request, "livros\catalogo.html")

def emprestimo(request):
    return render(request, "livros\emprestimo.html")













#Funções da sessao

def fun_section(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_form')
        email = request.POST.get('email_form')

        # Armazenando os dados na sessão
        request.session['nome_usuario'] = nome_usuario
        request.session['email'] = email

        return redirect('inicio')

    return render(request, 'sessao\section.html')

def delete_section(request):
        request.session.flush()
        return redirect('/')
        
        
