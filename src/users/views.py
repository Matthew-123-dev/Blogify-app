from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm as CUCF
from .forms import  UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView 

# Create your views here.
#Adding security features.
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authentication and logging in of user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {username}.')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

@csrf_protect
def register_view(request):
    if request.method == 'POST':
        register_form = CUCF(request.POST)
        #Handling form data
        if register_form.is_valid():
            user= register_form.save()
            #Logging in new user
            login(request,user)
            messages.success(request, f'User {user.username} registered successfully.')
            return redirect('home')  
        else:
            print(register_form.errors)  
    else:
        register_form = CUCF()
    return render(request, 'users/register.html', {'register_form': register_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)
            messages.info(request, 'Profile created for user.')
        elif u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def profile_detail_view(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile_detail.html', context)

@login_required
def profile_update(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile', pk=profile.pk)
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'users/profile_update.html', {'form': form})