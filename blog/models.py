from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	desctiption = models.TextField()  # fix to 'description' in production
	date = models.DateTimeField(default=timezone.now)
	like = models.ManyToManyField(User, blank=True, related_name='post_like')

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def get_like_url(self):
		return reverse('post-like', kwargs={'pk': self.pk})

	def get_api_like_url(self):
		return reverse('api-post-like', kwargs={'pk': self.pk})
	