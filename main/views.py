import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.timezone import now

from .forms import RegisterForm
from .models import *


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация количества студентов
    num_students = Student.objects.all().count()
    return render(
        request, 'index.html', context={
            'num_students': num_students,
            'student_list': Student.objects.all(),
        })


# функция отображения страницы с тестом, декортатор  login_required
# так как только аутенфицированые пользователи могут решать тесты
@login_required
def test(request):
    # открываем страницу с тестом
    f = open('main/static/test.json')
    # парсим json с тестом 'test_1' в собсвтенную структуру
    data = json.load(f)
    test_json = data['test_1']
    test_name = test_json['name']
    questions = []
    for question in test_json['questions']:
        task = question['question']
        answers = []
        for answer in question['answers']:
            answers.append(answer)

        correct_ans_ind = question['correct_answer'] - 1

        if correct_ans_ind > len(answers) or correct_ans_ind < 0:
            raise ValueError("test incorrect, correct answer cant be chosen")

        questions.append({'task': task, 'answers': answers, 'correct': answers[correct_ans_ind]})

    # если мы получичили не GET запрос а POST тогда надо записать данные о прохождении и сохранить в базу
    if request.method == 'POST':
        # считаем количество всех и правильных вопросов
        total = 0
        correct = []
        for q in questions:
            total += 1
            if request.POST.get(q['task']) == q['correct']:
                correct.append(total)

        percentage = len(correct) / total * 100
        print(total, correct, percentage)
        # сохраняем результат
        result_instance = Results.objects.create(percentage=percentage, finishedDate=now(), user=request.user)
        context = {
            "res": result_instance,
            "correct": correct,
        }
        # перенапрвялем на страницу с результатом
        return render(request, 'test_result.html', context)

    else:
        # если же был GET, тогда отправляем на страницу с тестом
        return render(
            request, 'test.html', context={
                'questions': questions,
                'test_name': test_name
            })


# страница с резульатами
def results(request):
    all_paginator = Paginator(Results.objects.all().order_by('-finishedDate'), 5)
    page_all_obj = all_paginator.get_page(request.GET.get('page_all'))

    page_user_obj = None

    # если пользователь произвел вход то можно показать его результаты
    if request.user.is_authenticated:
        user_results = Results.objects.filter(user=request.user).order_by('-finishedDate')
        user_paginator = Paginator(user_results, 5)
        page_user_obj = user_paginator.get_page(request.GET.get('page_user'))

    return render(
        request, 'results.html', context={
            'page_all_obj': page_all_obj,
            'page_user_obj': page_user_obj,
        })


def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

