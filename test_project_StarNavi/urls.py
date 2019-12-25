from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='log-in.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='log-out.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('', include('blog.urls')),  # This is used to using for including everything from urls.py which is located in blog directory;
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)