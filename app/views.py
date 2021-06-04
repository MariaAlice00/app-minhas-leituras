import os
from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro


def livro_list(request):
    search = request.GET.get('search')
    if search:
        livros = Livro.objects.filter(titulo__icontains=search)
    else:
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

        return redirect('livro_detail', pk=livro.pk)

    return render(request, 'app/livro_new.html', {'livros': livros})


def livro_edit(request, pk):
    livro = Livro.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(livro.imagem) > 0:
                os.remove(livro.imagem.path)
            livro.imagem = request.FILES['imagem']
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.genero = request.POST.get('genero')
        livro.serieunico = request.POST.get('serieunico')
        livro.nota = request.POST.get('nota')
        livro.opiniao = request.POST.get('opiniao')

        livro.save()

        return redirect('livro_detail', pk=livro.pk)

    return render(request, 'app/livro_edit.html', {'livro': livro})


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('livro_list')
