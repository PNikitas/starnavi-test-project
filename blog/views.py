from django.shortcuts import render
from .models import Post


def homePage(request):  # Logic for the main page;
    context = {
        'posts': Post.objects.all(),
    }
    
    return render(request, 'home-page.html', context)


