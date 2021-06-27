from django.db.models import fields 
from django.forms import ModelForm, models
from .models import Noticia

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = models.ALL_FIELDS


        