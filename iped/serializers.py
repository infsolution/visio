from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from iped.models import *



class PadariaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Padaria
		fields=('url', 'pk', 'nome', 'endereco', 'latitude','longitude' ,'owner', 'produtos')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	padarias = PadariaSerializer(many=True, read_only=True)
	class Meta:
		model = User
		fields=('url', 'username', 'padarias')

'''class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	padarias = PadariaSerializer(many=True, read_only=True)
	class Meta:
		model=Cliente
		fields=('url', 'pk', 'nome', 'padarias')'''

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
	padaria = serializers.SlugRelatedField(queryset=Padaria.objects.all(), slug_field='nome')
	class Meta:
		model = Produto
		fields=('url', 'nome', 'padaria', 'descricao','fabricacao', 'preco', 'foto')
class ItemSerializer(serializers.HyperlinkedModelSerializer):
	venda = serializers.SlugRelatedField(queryset=Venda.objects.all(), slug_field='pk')
	produto =serializers.SlugRelatedField(queryset=Produto.objects.all(), slug_field='nome')
	class Meta:
		model=Item
		fields=('url','venda', 'produto')
class VendaSerializer(serializers.HyperlinkedModelSerializer):
	padaria = serializers.SlugRelatedField(queryset=Padaria.objects.all(), slug_field='nome')
	cliente = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='nome')
	itens =ItemSerializer(many=True, read_only=True)
	class Meta:
		model = Venda
		fields=('url', 'padaria', 'cliente', 'valor', 'closed', 'dateFinish', 'itens')
	