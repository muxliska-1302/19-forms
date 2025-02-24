from django.shortcuts import render, redirect
from .forms import QuestionForm


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tests:list')
    else:
        form = QuestionForm()

    ctx = {'form':form}
    return render(request, 'tests/test-formset.html', ctx)