from django.db import models
from django.db.models.base import Model

# Modelo para noticias
class Autor(models.Model):
    idAutor = models.IntegerField(primary_key=True, verbose_name="ID Autor")
    nombreAutor = models.CharField(max_length=50, verbose_name="Nombre Autor")

    def __str__(self):
        return self.nombreAutor

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID Categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre Categoria")

    def __str__(self) -> str:
        return self.nombreCategoria

class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name="ID Noticia")
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    contenido = models.TextField(max_length=None, verbose_name="Contenido")
    fecha = models.DateField(verbose_name="Fecha publicacion")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo