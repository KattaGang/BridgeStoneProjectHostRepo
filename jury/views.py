from django.shortcuts import render, redirect
from idea.models import Idea
from program.models import Program, BusinessUnit
from account.models import Profile
from django.contrib.auth.models import User
from .forms import IdeaStatusForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def juryIdeaList(request):
    if not request.user.profile.is_jury:
        return redirect('access-denied')
    user = request.user
    business_units = BusinessUnit.objects.filter(jury=user)
    programs = Program.objects.filter(business_unit=None)
    for business_unit in business_units:
        programs = programs | Program.objects.filter(business_unit=business_unit)
    ideas = Idea.objects.filter(business_unit=business_unit)
    context = {
        'user': user,
        'programs': programs,
        'business_unit': business_unit,
        'ideas': ideas,
    }
    return render(request, 'jury/jury_idea_list.html', context)


@login_required(login_url='login')
def ideaAccept(request, pk):
    if not request.user.profile.is_jury:
        return redirect('access-denied')
    user = request.user
    idea = Idea.objects.get(id=pk)
    if user.profile.is_jury and user.profile.jury_business_unit == idea.business_unit:
        idea.accept()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('access-denied')


@login_required(login_url='login')
def ideaReject(request, pk):
    if not request.user.profile.is_jury:
        return redirect('access-denied')
    user = request.user
    idea = Idea.objects.get(id=pk)
    if user.profile.is_jury and user.profile.jury_business_unit == idea.business_unit:
        idea.reject()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('access-denied')


@login_required(login_url='login')
def ideaPutOnHold(request, pk):
    if not request.user.profile.is_jury:
        return redirect('access-denied')
    user = request.user
    idea = Idea.objects.get(id=pk)
    if user.profile.is_jury and user.profile.jury_business_unit == idea.business_unit:
        idea.putOnHold()
        idea.save()
        return redirect('jury-idea-list')
    return redirect('access-denied')

@login_required(login_url='login')
def ideaChangeStatus(request, pk):
    if not request.user.profile.is_jury:
        return redirect('access-denied')
    user = request.user
    idea = Idea.objects.get(id=pk)
    if idea.business_unit.jury == user:
        if request.method == 'POST':
            form = IdeaStatusForm(request.POST, request.FILES, instance=idea)
            if form.is_valid():
                idea = form.save()
                idea.change_of_status_mail()
                return redirect('idea', idea.id)
        form = IdeaStatusForm(instance=idea)
        context = {
            'form' : form,
        }
        return render(request, 'jury/idea_change_status.html', context)
    return redirect('access-denied')
