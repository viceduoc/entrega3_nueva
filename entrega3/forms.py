from django.db.models import fields 
from django.forms import ModelForm, models
from .models import Autor, Categoria, Noticia

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = models.ALL_FIELDS

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = models.ALL_FIELDS


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = models.ALL_FIELDS


        
        