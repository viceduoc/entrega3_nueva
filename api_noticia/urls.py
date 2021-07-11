from django.urls import path
from .views import noticias

urlpatterns = [
    path('noticias/', noticias, name='noticias'),
]