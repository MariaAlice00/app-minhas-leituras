from django.db import models


class Livro(models.Model):
    imagem = models.ImageField(upload_to='imagens')
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    serieunico = models.CharField(max_length=50)
    nota = models.FloatField()
    opiniao = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo
