from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from program.models import Program
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


@login_required(login_url='login')
def ideaView(request, pk):
    idea = Idea.objects.get(id=pk)
    jury = idea.business_unit.jury
    print(idea.business_unit, idea.business_unit.jury)
    context = {
        'idea': idea,
        'idea_status': idea.getStatus(),
        'jury': jury,
    }
    return render(request, 'idea/idea.html', context)


@login_required(login_url='login')
def ideaCreate(request, pk):
    program = Program.objects.get(id=pk)
    form = IdeaForm()
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        idea = form.save(commit=False)
        idea.program = program
        idea.business_unit = idea.program.business_unit
        idea.ideator = request.user
        if form.is_valid():
            idea.save()
            idea.send_apply_email()
            return redirect('idea', idea.id)
    context = {
        'form': form,
    }
    return render(request, 'idea/idea_form.html', context)


@login_required(login_url='login')
def ideaList(request):
    ideas = Idea.objects.all()
    context = {
        'ideas': ideas,
    }
    return render(request, 'idea/idea_list.html', context)


@login_required(login_url='login')
def ideaUpdate(request, pk):
    idea = Idea.objects.get(id=pk)
    if idea.ideator != request.user:
        return redirect('access-denied')
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context = {
            'form': form,
        }
        return render(request, 'idea/idea_form.html', context)
    else:
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        form.save()
        return redirect('idea', idea.id)
