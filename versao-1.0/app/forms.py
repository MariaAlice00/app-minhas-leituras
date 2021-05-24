from django.forms import ModelForm
from app.models import Livro


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero', 'serieunico', 'nota', 'opiniao']