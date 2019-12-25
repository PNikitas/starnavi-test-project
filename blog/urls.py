from django.urls import path
from .views import homePage


urlpatterns = [
    path('', homePage, name='home-page'),  # The main page of the website;
]