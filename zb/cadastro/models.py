from django.db import models

# Create your models here.

#Vou chamar a classe de alunos
class Alunos(models.Model):
 nome = models.CharField(max_length=100, null=False, blank=False)
 curso = models.CharField(max_length=100, null=False, blank=False)
 turma = models.CharField(max_length=100, null=False, blank=False)
 #Adicione esta função para exibir o nome dos alunos dentro do painel 
#administrativo
 #Veremos isso mais a frente
def __str__(self):
  return self.nome