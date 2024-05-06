from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Profile
from django.contrib import auth
from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm


User = get_user_model()
# 회원가입

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                email = request.POST['email'],)

            profile = Profile(
                user = user,
                nickname = request.POST['nickname'],
                image = request.FILES.get('profile_image'),)

            profile.save()

            auth.login(request, user)   
            return redirect('home')  
          
        return render(request, 'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html')
    return render(request, 'login.html' )

#로그아웃

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def profile(request):
    user_form = UpdateUserForm(request.POST or None, instance=request.user)
    profile_form = UpdateProfileForm(request.POST or None, request.FILES, instance=request.user.profile)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users-profile')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
