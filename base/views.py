from django.shortcuts import render
from program.models import Program, BusinessUnit
from django.contrib.auth.decorators import login_required
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')

@login_required(login_url='login')
def home(request):
    business_units = BusinessUnit.objects.all()
    programs = Program.objects.all()
    context = {
        'business_units': business_units,
        'programs' : programs,
    }
    return render(request, 'base/home.html', context)
