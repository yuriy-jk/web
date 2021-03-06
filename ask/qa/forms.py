from django import forms
from .models import Answer, Question
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth.models import User


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(min_length=5)
    username = forms.CharField(max_length=55)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
