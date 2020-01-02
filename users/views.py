from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post
from .forms import (UserSignupForm,
                    UserUpdateForm,
                    ProfileUpdateForm,
)


def signup(request):
    if request.method == 'POST':  # Our own form has method POST, that is why condition will be done
        form = UserSignupForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Welcome, {username}!')
            return redirect('login')
    else:
        form = UserSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'sign-up.html', context)


@login_required
def profile(request, pk):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, 
                                   instance=request.user
        )
        profile_form = ProfileUpdateForm(request.POST, 
                                         request.FILES, 
                                         instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'You have been just already changed your account info')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'posts': Post.objects.filter(author_id=request.user.id),
    }

    return render(request, 'profile.html', context)