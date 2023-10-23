from django.db import models

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(blank=True)
    texto = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    