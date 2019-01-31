 # -*- coding: utf-8 -*-
from django.urls import path
from iped import views
urlpatterns = [
    path('padaria/',views.PadariaList.as_view(), name=views.PadariaList.name),
    path('padaria/<int:pk>',views.PadariaDetail.as_view(), name=views.PadariaDetail.name),
    path('users/',views.UserList.as_view(),name=views.UserList.name),
	path('users/<int:pk>/',views.UserDetail.as_view(),name=views.UserDetail.name),
	path('produto/',views.ProdutoList.as_view(),name=views.ProdutoList.name),
	path('produto/<int:pk>/',views.ProdutoDetail.as_view(),name=views.ProdutoDetail.name),
]
