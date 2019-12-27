from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    PostLikeToggle,
                    PostLikeAPIToggle,
                    # UserPostListView,
)


urlpatterns = [
    path('', 
         PostListView.as_view(), 
         name='home-page'), 

    path('post/<int:pk>/', 
         PostDetailView.as_view(), 
         name='post-detail'),

    path('new-post/', 
         PostCreateView.as_view(), 
         name='post-create'),

    path('post/<int:pk>/update/', 
         PostUpdateView.as_view(), 
         name='post-update'),

    path('post/<int:pk>/delete/', 
         PostDeleteView.as_view(), 
         name='post-delete'),

    path('post/<int:pk>/like/', 
         PostLikeToggle.as_view(), 
         name='post-like'),

    path('api/post/<int:pk>/like/', 
         PostLikeAPIToggle.as_view(), 
         name='api-post-like'),

    # path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
]