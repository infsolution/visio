from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from iped.models import *
from iped.serializers import *
from iped.permissions import *

class PadariaList(generics.ListCreateAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	name = 'padaria-list'
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly,)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class PadariaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Padaria.objects.all()
	serializer_class = PadariaSerializer
	name='padaria-detail'
'''class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'''

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def perform_create(self, serializer):
		user = User(username=self.request.POST['username'],
					email=self.request.POST['email'])
		user.save()
		user.set_password(self.request.POST['password'])
		user.save()
	name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'	

'''class ClienteList(generics.ListCreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	name = 'cliente-list'
	def perform_create(self, serializer):
		serializer.save(usuario=self.request.user)
class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	name='cliente-detail'''
	

class ProdutoList(generics.ListCreateAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	name = 'produto-list'
class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Produto.objects.all()
	serializer_class = ProdutoSerializer
	name='produto-detail'	
