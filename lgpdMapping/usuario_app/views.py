from django.shortcuts import render
from usuario_app.models import Usuario, Perfil
from django.http import JsonResponse
from .serializers import UsuarioSerializer, PerfilSerializer, UsuarioReadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_rw_serializers import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


# def usuario_listar(request):
#     usuarios = Usuario.objects.all()
#     usuarios_lista = {
#         "usuarios": list(usuarios.values())
#     }
#     return JsonResponse(usuarios_lista)

@api_view(['GET'])
def usuario_list(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioReadSerializer(usuarios, many=True)
    return Response(serializer.data)

# def usuario_by_id(request, pk):
#     usuario = Usuario.objects.get(pk=pk)
#     usuario_exibir = {
#         "usuario": {
#             "nome": usuario.nome,
#             "email": usuario.email,
#             "senha": usuario.senha,
#             "active": usuario.active,
#         }
#     }

#     return JsonResponse(usuario_exibir)

@api_view(['GET'])
def usuario_by_id(request, pk):
    usuario = Usuario.objects.get(id=pk)
    serializer = UsuarioReadSerializer(usuario, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def usuario_create(request):
    serializer = UsuarioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Falso")
    return Response(serializer.data)

@api_view(['PUT'])
def usuario_update(request, pk):
    usuario = Usuario.objects.get(id=pk)
    serializer = UsuarioSerializer(instance=usuario, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:  return Response('False')
    return Response(serializer.data)

@api_view(['DELETE'])
def usuario_delete(request, pk):
    usuario = Usuario.objects.get(id=pk)
    usuario.delete()

    return Response('Usuário Excluído com sucesso')


# Perfil de Usuário

@api_view(['GET'])
def perfil_list(request):
    perfis = Perfil.objects.all()
    serializer = PerfilSerializer(perfis, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def perfil_by_id(request, pk):
    perfil = Perfil.objects.get(id=pk)
    serializer = PerfilSerializer(perfil, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def perfil_create(request):
    serializer = PerfilSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def perfil_update(request, pk):
    perfil = Perfil.objects.get(id=pk)
    serializer = PerfilSerializer(instance=perfil, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def perfil_delete(request, pk):
    perfil = Perfil.objects.get(id=pk)
    perfil.delete()

    return Response('Perfil Excluído com sucesso')


# class RegistrationAPIView(APIView):
#     # Allow any user (authenticated or not) to hit this endpoint.
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         user = request.data.get('usuario', {})

#         # The create serializer, validate serializer, save serializer pattern
#         # below is common and you will see it a lot throughout this course and
#         # your own work later on. Get familiar with it.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         user = request.data.get('user', {})

#         # Notice here that we do not call `serializer.save()` like we did for
#         # the registration endpoint. This is because we don't  have
#         # anything to save. Instead, the `validate` method on our serializer
#         # handles everything we need.
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)