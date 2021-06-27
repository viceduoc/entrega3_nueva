from entrega3.forms import NoticiaForm
from django.shortcuts import render, redirect
from .models import Noticia

# Create your views here.
def home(request):
    return render(request, 'entrega3/home.html')

# agrengando segundo template al view 
def formulario(request):
    return render(request, 'entrega3/formulario.html')

def noticias(request):
    noticias = Noticia.objects.all()
    datos = {
        'noticias' : noticias
    }
    return render(request, 'entrega3/noticias.html', datos)

def eliminarNoticia(request, id):
    noticia = Noticia.objects.get(idNoticia=id)
    noticia.delete()

    return redirect(to="noticias")

# Agregar noticia
def agregarNoticia(request):
    datos = {
        'form': NoticiaForm() 
        }
    if request.method == 'POST':
        formulario_add = NoticiaForm(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()
            datos['mensaje'] = "Noticia publicada"

    return render(request, 'entrega3/agregaNoticia.html', datos)


def editarNoticia(request,id):
    noticia = Noticia.objects.get(idNoticia=id)
    datos = {
        'form': NoticiaForm(instance=noticia) 
        }

    if request.method == 'POST':
        formulario_add = NoticiaForm(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()
            datos['mensaje'] = "Noticia editada"
            
    return render(request, 'entrega3/editarNoticia.html', datos)