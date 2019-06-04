 # -*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from makevisio import views
urlpatterns = [
	path('',views.index, name='index'),
	path('buscar',views.search_google, name='buscar_item'),
	path('page/',views.get_page, name='page'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)