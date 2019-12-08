from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, verbose_name='Name')

class Deal(models.Model):
	name = models.CharField(max_length=128, verbose_name='Name')

class Topic(models.Model):
	name = models.CharField(max_length=128, verbose_name='Name')	
