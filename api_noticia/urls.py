from django.urls import path
from api_noticia.views import noticias, noticia
from rest_app.viewsLogin import login

urlpatterns = [
    path('noticias', noticias, name='noticias'),
    path('noticia/<int:pk>', mascota, name="noticia" ),
    path('login/',login,name='login' )


]