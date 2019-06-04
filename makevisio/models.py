from django.db import models

class Audio(models.Model):
	nome = models.CharField(max_length=255, null=False)
	
