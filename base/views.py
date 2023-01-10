from django.shortcuts import render, redirect
from program.models import Program, BusinessUnit
from django.contrib.auth.decorators import login_required
from idea.models import Idea
from account.models import Invitation
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


@login_required(login_url='login')
def home(request):
    business_units = BusinessUnit.objects.all()
    programs = Program.objects.all()
    context = {
        'business_units': business_units,
        'programs': programs,
    }
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def adminPanel(request):
    if not request.user.profile.is_admin:
        return redirect('access-denied')
    ideas = Idea.objects.all()
    no_ideas = []
    for st, fi in Idea.STATUS_CHOICES:
        no_ideas.append(ideas.filter(status=st).count())
    invitations = Invitation.objects.filter(admin=request.user)
    context = {
        'invitations' : invitations,
        'number_ideas' : {
            "Complete" : ideas.filter(status=3).count(),
            "Paused" : ideas.filter(status=4).count(),
            "Active" : ideas.filter(status=1).count(),
            "Handoff" : ideas.filter(status=2).count(),
            "Stopped" : ideas.filter(status=5).count(),
        },
    }
    return render(request, 'base/admin_panel.html', context)
