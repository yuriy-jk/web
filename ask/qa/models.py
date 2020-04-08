from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_absolute_url(self):
        return (reverse('question', kwargs={'id': self.id}))

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
