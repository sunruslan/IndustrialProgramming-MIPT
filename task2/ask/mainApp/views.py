from django.shortcuts import render
from mainApp.models import Questions
from django.http import HttpResponseRedirect
from mainApp.forms import QuestionForm


def index(request):
    context_dict = {'questions': Questions.objects.all().order_by('-date')[:30]}
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_done = False
            instance.save()
    form = QuestionForm()
    context_dict['question_add_form'] = form
    return render(request, 'mainApp/homePage.html', context_dict)
