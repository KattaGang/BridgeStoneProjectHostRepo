from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, InvitationForm
from .models import Profile, Invitation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from program.models import BusinessUnit
# Create your views here.


def dummyView(request, pk=0, pk2=0):
    return render(request, 'dummy.html')


def baseView(request):
    return redirect('home')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Username or Password')
    context = {
        'messages': messages,
    }
    return render(request, 'account/login.html', context)


def registerUser(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    else:
        user_form = UserCreationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = request.POST.get('email')
            profile = Profile(user=user)
            user.save()
            profile.save()
            login(request, user)
            return redirect('profile-update')
        else:
            context = {
                'user_form': user_form,
                'messages': messages,
            }
            return render(request, 'account/register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userProfile(request):
    return redirect('profile', request.user.id)


def profile(request, pk):
    user = User.objects.get(id=pk)
    invitations = Invitation.objects.filter(email=user.email)
    context = {
        'user': user,
        'invitations' : invitations,
    }
    return render(request, 'account/profile.html', context)


def profileList(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'account/profile_list.html', context)


@login_required(login_url='login')
def profileUpdate(request):
    profile = request.user.profile
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            profile.save()
            return redirect('profile', profile.id)
        else:
            errors = profile_form.errors.as_data()
            for field in errors:
                for error in errors[field]:
                    messages.error(request, error)
    context = {
        'form': profile_form,
        'messages': messages,
    }
    return render(request, 'account/profile_form.html', context)


@login_required(login_url='login')
def inviteUser(request):
    if not request.user.profile.is_admin:
        return redirect('access-denied')
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        invite = form.save(commit=False)
        if request.POST.get('r1'):
            invite.post = 'Admin'
        else:
            invite.post = 'Jury'
        invite.admin = request.user
        invite.save()
        return redirect('admin-panel')
    business_units = BusinessUnit.objects.all()
    context = {
        'business_units' : business_units,
        'form' : InvitationForm(),
    }
    return render(request, 'account/invitation_form.html', context)


@login_required(login_url='login')
def viewInvitation(request, pk):
    invitation = Invitation.objects.get(id=pk)
    if (request.user.email != invitation.email) and (request.user != invitation.admin):
        return redirect('access-denied')
    if request.method == 'POST':
        if request.user.email != invitation.email:
            return redirect('access-denied')
        if invitation.post == 'Admin':
            request.user.profile.is_admin = True
        else:
            request.user.profile.is_jury = True
            invitation.business_unit.jury = request.user
            invitation.business_unit.save()
        request.user.profile.save()
        return redirect('user-profile')
    context = {
        'invitation': invitation,
    }
    return render(request, 'account/invitation.html', context)

@login_required(login_url='login')
def withdrawInvitation(request, pk):
    if not request.user.profile.is_admin:
        return redirect('access-denied')
    invitation = Invitation.objects.get(id=pk)
    invitation.delete()
    return redirect('admin-panel')

def accessDenied(request):
    return render(request, 'access_denied.html')
