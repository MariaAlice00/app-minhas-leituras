from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro


def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'app/livro_list.html', {'livros': livros})


def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'app/livro_detail.html', {'livro': livro})


def livro_new(request):
    livros = Livro.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        livro = Livro.objects.create(
            titulo=data['titulo'],
            autor=data['autor'],
            genero=data['genero'],
            serieunico=data['serieunico'],
            nota=data['nota'],
            opiniao=data['opiniao'],
            imagem=image,
        )

        return redirect('livro_list')

    return render(request, 'app/livro_new.html', {'livros': livros})
