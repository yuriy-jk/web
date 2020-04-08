from django import forms
from .models import Answer, Question

class AskForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text', 'question']
