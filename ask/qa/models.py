from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Model):
	def new(self):
		return self.order_by('-addet_at')
	def popular(self):
		return self.order_by('-rating')


class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_lenght=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='question_like_user')


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	question = models.ForeignKey('Question')
	author = models.ForeignKey(User)