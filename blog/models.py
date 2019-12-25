from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Post fields
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	desctiption = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title