from django.urls import path
from django.views.generic import ListView

from .views import *


urlpatterns = [
    path('', main_page, name='main'),
    path('<slug:language>', language, name='language'),
    path('search/', search, name='search')
]
