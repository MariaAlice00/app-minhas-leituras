from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    serieunico = models.CharField(max_length=50)
    nota = models.FloatField()
    opiniao = models.CharField(max_length=300)
