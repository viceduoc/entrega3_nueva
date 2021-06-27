from django.contrib import admin

from .models import Autor, Categoria, Noticia

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Autor)

