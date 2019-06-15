from django.core.files.storage import FileSystemStorage
from django.db import models

class Atribut(models.Model):
	name = models.CharField(max_length=255, null=False)
	name_audio = models.CharField(max_length=2048, null=False)
	id_name = models.CharField(max_length=255, null=False)
	description = models.CharField(max_length=255, null=False)
	path_audio = models.CharField(max_length=2048, null=False)
	id_description = models.CharField(max_length=255, null=False)

	
