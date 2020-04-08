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


#class AskForm(forms.Form):
	#title = forms.CharField(max_length=100)
	#text = forms.CharField(widget=forms.Textarea)

	#def clean(self):
		#return self.cleaned_data

	#def save(self):
		#ask = self.cleaned_data
		#return ask


#class AnswerForm(forms.Form):
	#text = forms.CharField(widget=forms.Textarea)
	#question = forms.IntegerField()

	#def clean(self):
		#return self.cleaned_data

	#def save(self):
		#answer = self.cleaned_data
		#return answer