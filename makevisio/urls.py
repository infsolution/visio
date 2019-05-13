 # -*- coding: utf-8 -*-
from django.urls import path
from makevisio import views
urlpatterns = [
	path('',views.index, name='index'),
	path('buscar',views.search_google, name='buscar_item'),
	path('page/',views.get_page, name='page'),
]
