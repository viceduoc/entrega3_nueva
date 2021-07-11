from django.urls import path
from api_noticia.views import noticias

urlpatterns = [
    path('noticias', noticias, name='noticias'),
]