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
