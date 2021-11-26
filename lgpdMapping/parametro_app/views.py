from django.shortcuts import render
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def listar_categoria(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoria_by_id(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(categoria, many=False)
    return Response(serializer.data)

