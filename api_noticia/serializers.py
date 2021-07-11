from django.db.models import fields
from rest_framework import serializers
from entrega3.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Noticia
        fields = ['idNoticia', 'titulo', 'contenido', 'fecha', 'categoria', 'autor', 'imagen']