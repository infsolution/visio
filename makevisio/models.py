from django.core.files.storage import FileSystemStorage
from django.db import models



class Atribut(models.Model):
	name = models.CharField(max_length=255, null=False)
	name_audio = models.CharField(max_length=2048, null=False)
	id_name = models.CharField(max_length=255, null=False)

class Item(models.Model):
	description = models.TextField()
	path_audio = models.CharField(max_length=2048, null=False)
	id_description = models.CharField(max_length=255, null=False)
	atributo = models.ForeignKey(Atribut, on_delete=models.CASCADE, related_name='items')

class LinkAtribut(models.Model):
	link = models.CharField(max_length=255, null=False)
	displayLink = models.CharField(max_length=255, null=False)
	displayLink_audio = models.CharField(max_length=1024, null=False)
	displayLink_id = models.CharField(max_length=255, null=False)
	title = models.CharField(max_length=255, null=False)
	title_audio = models.CharField(max_length=1024, null=False)
	title_id = models.CharField(max_length=255, null=False)
	snippet = models.CharField(max_length=255, null=False)
	snippet_audio = models.CharField(max_length=1024, null=False)
	snippet_id = models.CharField(max_length=255, null=False)