from django.shortcuts import render, redirect
from .models import Program, BusinessUnit
from .forms import ProgramForm, BusinessUnitForm
from idea.models import Idea
from django.contrib.auth.decorators import login_required
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')

@login_required(login_url='login')
def programList(request):    
    programs = Program.objects.all()
    context = {
        'programs': programs,
    }
    return render(request, 'program/program_list.html', context)

@login_required(login_url='login')
def programView(request, pk):
    program = Program.objects.get(id=pk)
    ideas = Idea.objects.filter(program=program)
    context = {
        'program': program,
        'ideas' : ideas,
    }
    return render(request, 'program/program.html', context)

@login_required(login_url='login')
def programCreate(request):
    if not request.user.profile.is_admin:
        return redirect('unauthorized_access')
    if request.method == 'GET':
        form = ProgramForm()
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.coordinator = request.user
            program.save()
            return redirect('program', program.id)
        else:
            context = {
                'form' : form,
            }
            return render(request, 'program/program_form.html', context)


@login_required(login_url='login')
def programUpdate(request, pk):
    program = Program.objects.get(id=pk)
    print(program.name)
    if request.method == 'GET':
        form = ProgramForm(instance=program)
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program', program.id)
        context = {
            'form': form
        }
        return render(request, 'program/program_form.html', context)



@login_required(login_url='login')
def programDelete(request, pk):
    program = Program.objects.get(id=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program-list')
    else:
        context = {
            'program' : program,
        }
        return render(request, 'program/program_delete_confirmation.html')




@login_required(login_url='login')
def businessUnitList(request):    
    business_units = BusinessUnit.objects.all()
    context = {
        'business_units': business_units,
    }
    return render(request, 'program/business_unit_list.html', context)

@login_required(login_url='login')
def businessUnitView(request, pk):
    business_unit = business_unit.objects.get(id=pk)
    programs = Program.objects.filter(business_unit=business_unit)
    ideas = Idea.objects.filter(business_unit=business_unit)
    context = {
        'business_unit': business_unit,
        'programs' : programs,
        'ideas' : ideas,
    }
    return render(request, 'program/business_unit.html', context)



@login_required(login_url='login')
def businessUnitCreate(request):
    if not request.user.profile.is_admin:
        return redirect('unauthorized_access')
    if request.method == 'GET':
        form = BusinessUnitForm()
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = BusinessUnitForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.save()
            return redirect('admin-panel')
        else:
            context = {
                'form' : form,
            }
            return render(request, 'program/program_form.html', context)


@login_required(login_url='login')
def businessUnitUpdate(request, pk):
    business_unit = BusinessUnit.objects.get(id=pk)
    if request.method == 'GET':
        form = BusinessUnitForm(instance=business_unit)
        context = {
            'form': form,
        }
        return render(request, 'program/program_form.html', context)
    else:
        form = BusinessUnitForm(request.POST, instance=business_unit)
        if form.is_valid():
            form.save()
            return redirect('program', business_unit.id)
        context = {
            'form': form
        }
        return render(request, 'program/program_form.html', context)



@login_required(login_url='login')
def businessUnitDelete(request, pk):
    business_unit = BusinessUnit.objects.get(id=pk)
    if request.method == 'POST':
        business_unit.delete()
        return redirect('program-list')
    else:
        context = {
            'program' : business_unit,
        }
        return render(request, 'program/business_unit_delete_confirmation.html')