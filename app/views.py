from django.shortcuts import render, redirect
from authentication.models import CustomerModel
from .models import *

context = {}

def welcomePage(request):
    return render(request, "welcome.html", context)


def homePage(request):
    return render(request, "home.html", context)


def gamePage(request):
    return render(request, "game.html", context)


def madBlockPage(request):
    return render(request, "Madblock.html", context)


def academicsPage(request):
    try:
        context["classes"] = ClassModel.objects.all().order_by("std")
        if request.method == 'POST':
            std = request.POST.get('std')
            return redirect(f"../subjects/{std}/")
    except Exception as e:
        print(e)
    return render(request, "Academics-class.html", context)


def subjectPage(request, class_id):
    try:
        context["subjects"] = SubjectsModel.objects.filter(std=ClassModel.objects.get(std=class_id))
        if request.method == 'POST':
            subject = request.POST.get('subject')
            return redirect(f"../../chapters/{subject}/")
    except Exception as e:
        print(e)
    return render(request, "academics-subject.html", context)


def chapterPage(request, subject_id):
    try:
        context["chapters"] = ChapterModel.objects.filter(subject=SubjectsModel.objects.get(subject_name=subject_id))
        if request.method == 'POST':
            chapter = ChapterModel.objects.get(id=request.POST.get('chapter'))
            context["download"] = chapter.link
        pass
    except Exception as e:
        print(e)
    return render(request, "academics-chapter.html", context)


def avatarPage(request):
    try:
        user = CustomerModel.objects.get(email=request.user.email)
        context["name"] = user.name
    except Exception as e:
        print(e)
    return render(request, "avatar-page.html", context)


def helpPage(request):
    return render(request, "Help-support.html", context)


def quizPage(request):
    return render(request, "Quiz.html", context)

