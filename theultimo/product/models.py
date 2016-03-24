from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length = 200)
	application = models.TextField()
	description = models.TextField()
	characteristics = models.TextField()
	size = models.CharField(max_length = 300)
	surface = models.CharField(max_length = 200)
	thickness = models.CharField(max_length = 200)
	image = models.FileField(null=True, blank = True)
	updated = models.DateTimeField(auto_now=True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)


	def __unicode__(self):
			return self.title

	def __str__(self):
		return self.title

class Item(models.Model):
	title = models.CharField(max_length = 200)
	imageLink = models.FileField(null = False, blank = False)
	product = models.ForeignKey(Product)
	updated = models.DateTimeField(auto_now=True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)



	def __unicode__(self):
			return self.title

	def __str__(self):
		return self.title
