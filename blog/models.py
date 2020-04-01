from django.db import models
import datetime

class Post(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.title