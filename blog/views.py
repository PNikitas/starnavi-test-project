from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  RedirectView,
)


class PostListView(ListView):
    model = Post
    template_name = 'home-page.html'
    context_object_name = 'posts'
    paginate_by = 5


'''
class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Post.objects.filter(author=user)
'''


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'desctiption',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'desctiption',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        return True if self.request.user == post.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()

        return True if self.request.user == post.author else False


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        obj = get_object_or_404(Post, pk=post.id)
        user_one = self.request.user

        if user_one.is_authenticated:
            obj.like.remove(user_one) if user_one in obj.like.all() else obj.like.add(user_one)
        
        return obj.get_absolute_url()


class PostLikeAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, pk=None, format=None):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        obj = get_object_or_404(Post, pk=post.id)
        user_one = self.request.user
        updated = liked = False

        if user_one.is_authenticated:
            if user_one in obj.like.all():
                liked = False
                obj.like.remove(user_one)
            else:
                liked = True
                obj.like.add(user_one)
        
            updated = True

        counts = obj.like.count()
        
        context = {
            "updated": updated,
            "liked":   liked,
            "likescount": counts
        }

        return Response(context)


def homePage(request):  
    return render(request, 'home-page.html', {'posts': Post.objects.all()})