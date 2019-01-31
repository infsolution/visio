from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models

class Padaria(models.Model):
	favoritos = models.ManyToManyField(User)
	nome = models.CharField(max_length=80)
	endereco = models.CharField(max_length=80)
	latitude = models.DecimalField(max_digits=10, decimal_places=8)
	longitude = models.DecimalField(max_digits=10, decimal_places=8)
	owner = models.OneToOneField('auth.User', related_name='padaria_owner', on_delete=models.CASCADE)
	class Meta:
		ordering = ('nome',)
	def __str__(self):
		return self.nome

class Produto(models.Model):
	padaria = models.ForeignKey(Padaria, related_name='produtos', on_delete=models.CASCADE)
	nome = models.CharField(max_length=80)
	descricao = models.CharField(max_length=256)
	foto = models.ImageField(blank=True, null=True, upload_to='media/')
	fabricacao = models.DateTimeField(auto_now_add=False)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
	class Meta:
		ordering = ('nome',)
	def __str__(self):
		return self.nome

class Venda(models.Model):
	padaria = models.ForeignKey(Padaria, related_name='vendas', on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, related_name='compras', on_delete=models.SET_NULL, null=True)
	valor = models.DecimalField(max_digits=8, decimal_places=2)
	closed = models.BooleanField(default=False)
	dateFinish = models.DateTimeField(auto_now_add=False, blank=True, null=True)


class Item(models.Model):
	venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
	produto = models.ForeignKey(Produto, related_name='produto', on_delete=models.SET_NULL, null=True)

