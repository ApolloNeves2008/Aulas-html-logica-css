from django.db import models

# Create your models here.

from django.db import models

class livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    genero = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    disponivel = models.BooleanField(default=True)  

    def __str__(self):
        return self.titulo
    


    

