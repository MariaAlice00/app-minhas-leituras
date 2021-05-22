from django.shortcuts import render, redirect
from app.forms import LivroForm
from app.models import Livro


def home(request):
    data = {}
    data['db'] = Livro.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = LivroForm()
    return render(request, 'form.html', data)


def create(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Livro.objects.get(pk=pk)
    return render(request, 'view.html', data)
