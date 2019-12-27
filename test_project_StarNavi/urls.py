from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', 
         admin.site.urls),

    path('signup/', 
         user_views.signup, 
         name='signup'),

    path('login/', 
         auth_views.LoginView.as_view(template_name='log-in.html'), 
         name='login'),

    path('logout/', 
         auth_views.LogoutView.as_view(template_name='log-out.html'), 
         name='logout'),

    path('profile/<int:pk>/', 
         user_views.profile, 
         name='profile'),

    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name='password-reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password-reset-done'),

     path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name='password-reset-confirm'),

     path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password-reset-complete'),

    path('', 
        include('blog.urls')),  

    path('', 
        include('django.contrib.auth.urls')),

    path('api/token/', 
        TokenObtainPairView.as_view()),

    path('api/token/refresh/', 
        TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)