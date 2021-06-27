from django.conf.urls import url
from django.urls import path
from .views import home, formulario, noticias, eliminarNoticia



# Agregando path's
urlpatterns = [
    path('', home, name="home"),
    path('formulario', formulario, name="formulario"),
    path('noticias', noticias, name='noticias'),
    path('eliminar-noticia/<id>', eliminarNoticia, name="eliminar-noticia")
]