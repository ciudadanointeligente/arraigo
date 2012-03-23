from django.db import models

# Create your models here.

class Circunscripcion(models.Model):
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class District(models.Model):
	circunscripcion = models.ForeignKey('Circunscripcion')
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Comuna(models.Model):
	region = models.ForeignKey('Region')
	district = models.ForeignKey('District')
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Region(models.Model):
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name
	
