from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Question, Answer
from django.views.decorators.http import require_GET
from .forms import AnswerForm, AskForm, SignUpForm, LoginForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def test(request, *args, **kwargs):
	return HttpResponse('Ok')


def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('new'))


def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save()
		username = request.POST['username']
		my_password = request.POST['password']
		user = authenticate(request, username=username, password=my_password)
		if user is not None:
			login(request, user)
		return HttpResponseRedirect(reverse('new'))
	else:
		form = LoginForm()
		return render(request, 'qa/login.html', {'form': form})


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
		username = form.cleaned_data.get('username')
		my_password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=my_password)
		login(request, user)
		return HttpResponseRedirect(reverse('new'))
	else:
		form = SignUpForm()
		return render(request, 'qa/signup.html', {'form': form})


def index(request):
	return render(request, 'qa/index.html')


def ask(request):
	if request.method != 'POST':
		form = AskForm()
		return render(request, 'qa/ask.html', {'form': form})
	else:
		form = AskForm(request.POST)
		#form._user = request.user
		if form.is_valid():
			new_question = form.save()
			new_question.author = request.user
			new_question.save()
			url = new_question.get_absolute_url()
			return HttpResponseRedirect(url)


#@require_GET
def question(request, id):
	question = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		#form.author = request.user
		if form.is_valid():
			new_answer = form.save()
			new_answer.author = request.user
			new_answer.question = question
			new_answer.save()
			return HttpResponseRedirect(reverse('question', args=[id]))
	else:
		question = get_object_or_404(Question, id=id)
		form = AnswerForm(initial={'question': id})
	return render(request, 'qa/question.html', {
		'question': question,
		'answers': answers,
		'form': form
		})


def questions(request):
	questions = Question.objects.order_by('-added_at')
	context = {'questions': questions}
	return render(request, 'qa/questions.html', context)


def new(request):
	new_list = Question.objects.new()
	paginator = Paginator(new_list, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'qa/new.html', {
		'page_obj': page_obj
		})


def popular(request):
	pop_list = Question.objects.popular()
	paginator = Paginator(pop_list, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'qa/popular.html', {
		'page_obj': page_obj
		})


