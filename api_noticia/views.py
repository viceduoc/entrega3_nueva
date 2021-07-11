from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import NoticiaSerializer
from entrega3.models import Noticia
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view



from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['GET', 'POST'])
def noticias(request):
#     **-----------------------------**
#       LISTANDO TODOS LAS NOTICIAS
#     **-----------------------------** 
    if request.method == 'GET':
       lista_noticia = Noticia.objects.all()
       Serializer = NoticiaSerializer(lista_noticia, many=True) 
       return Response(Serializer.data)
    
#     **-----------------------------**
#       AGREGANDO UNA NOTICIA
#     **-----------------------------** 

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     **----------------------------------**
#       AGREGAR UNA ACTUALIZACION ELIMINAR
#     **----------------------------------** 

@api_view(['GET', 'PUT', 'DELETE'])
def noticia(request, pk):
    """
    Instanciar el elemento singular desde la base de datos
    """
    try:
        noticia = Noticia.objects.get(idNoticia=pk)
    except Noticia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoticiaSerializer(noticia)
        return Response(serializer.data)

    """
    ACTUALIZA LOS DATOS
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(noticia, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
        """
        ELIMINA
        """
    elif request.method == 'DELETE':
            
            noticia.delete()
            return Response(status =status.HTTP_204_NO_CONTENT)