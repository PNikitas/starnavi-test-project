from django.urls import path, include
from rest_framework import routers
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    PostLikeToggle,
                    PostLikeAPIToggle,
                    PostView,
                    UserPostListView,
                    ProfileView,
                    apiHelp,
)


router = routers.DefaultRouter()
router.register('blog', PostView)

router_profile = routers.DefaultRouter()
router_profile.register('profile', ProfileView)

urlpatterns = [
     path('', 
          PostListView.as_view(), 
          name='home-page'),

     path('user/<str:username>/', 
          UserPostListView.as_view(), 
          name='user-posts'),  

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

     path('api/help/',
           apiHelp,
           name='api-help'),

     path('api/posts/', include(router.urls)),

     path('api/profiles/', include(router_profile.urls)),
]