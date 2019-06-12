from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media')
class Audio(models.Model):
	nome = models.CharField(max_length=255, null=False)
	#path = 
	
