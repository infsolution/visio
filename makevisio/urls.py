 # -*- coding: utf-8 -*-
from django.urls import path
from makevisio import views
urlpatterns = [
	path('',views.index, name='index'),
	path('buscar',views.search_google, name='buscar_item'),
	path('api/iped/padaria/',views.PadariaList.as_view(), name=views.PadariaList.name),
	path('api/iped/padaria/<int:pk>',views.PadariaDetail.as_view(), name=views.PadariaDetail.name),
	path('api/iped/users/',views.UserList.as_view(),name=views.UserList.name),
	path('api/iped/users/<int:pk>/',views.UserDetail.as_view(),name=views.UserDetail.name),
	path('api/iped/produto/',views.ProdutoList.as_view(),name=views.ProdutoList.name),
	path('api/iped/produto/<int:pk>/',views.ProdutoDetail.as_view(),name=views.ProdutoDetail.name),
]
