from django.urls import path
from api_noticia.views import noticias, noticia
from api_noticia.viewsLogin import login

urlpatterns = [
    path('noticias', noticias, name='noticias'),
    path('noticia/<int:pk>', noticia, name="noticia" ),
    path('login/',login,name='login' )


]