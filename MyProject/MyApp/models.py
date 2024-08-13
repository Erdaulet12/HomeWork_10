from django.db import models


class MyModel(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	address = models.CharField(max_length=255)
	email = models.EmailField()

	def __str__(self):
		return self.name
