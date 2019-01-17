 # -*- coding: utf-8 -*-
from django.urls import path, include
from makevisio import views
urlpatterns = [
    path('',views.index, name='index'),
    path('search',views.search_google, name='busca'),
]