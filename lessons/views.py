from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson
from .forms import LessonForm


def lessons_list(request):
    lessons = Lesson.objects.all()
    ctx = {'lessons':lessons}
    return render(request, 'lessons/lesson-list.html', ctx)

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lessons:list')
    else:
        form = LessonForm()

    ctx = {'form':form}
    return render(request, 'lessons/lesson-create.html', ctx)

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    tests = lesson.tests.all()
    ctx = {'lesson':lesson, 'tests':tests}
    return render(request, 'lessons/lesson-detail.html', ctx)

def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.delete()
    return redirect('lessons:list')

def edit_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lessons:list')
    else:
        form = LessonForm(instance=lesson)
    ctx = {
        'form':form,
        'lesson':lesson
    }
    return render(request, 'lessons/lesson-create.html', ctx)