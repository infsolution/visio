from django.urls import path, include
from makevisio import views
urlpatterns = [
    path('',views.index, name='index'),
]