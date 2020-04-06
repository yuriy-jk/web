from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer
from django.views.decorators.http import require_GET


 
def test(request, *args, **kwargs):
	return HttpResponse('Ok')


def index(request):
	return render(request, 'qa/index.html')

@require_GET
def question(request, id):
	question = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=id)
	return render(request, 'qa/question.html', {
		'question': question,
		'answers': answers
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


