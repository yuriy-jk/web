from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Question, Answer
from django.views.decorators.http import require_GET
from .forms import AnswerForm, AskForm
from django.urls import reverse


 
def test(request, *args, **kwargs):
	return HttpResponse('Ok')


def index(request):
	return render(request, 'qa/index.html')


def ask(request):
	if request.method != 'POST':
		form = AskForm()
		return render(request, 'qa/ask.html', {'form': form })
	else:
		form = AskForm(request.POST)
		if form.is_valid():
			#form.clean()
			new_question = form.save()
			#new_question = Question()
			new_question.save()
			url = new_question.get_absolute_url()
			#return HttpResponseRedirect('question', args=[id])
			#url = new_question.get_absolute_url()
			#return HttpResponseRedirect(reverse('question'))
			#print(url)
			return HttpResponseRedirect(url)
			#return HttpResponseRedirect(reverse('question', kwargs={'id': self.id}))
			#return render(request, 'qa/question.html')


#@require_GET
def question(request, id):
	question = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=id)
	#question_id = request.GET.get('question')
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			new_answer = form.save()
			new_answer.question = question
			new_answer.save()
			return HttpResponseRedirect(reverse('question', args=[id]))
	else:
		#question_id = question.id
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


