 # -*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from makevisio import views
urlpatterns = [
	path('',views.index, name='index'),
	path('buscar',views.search_google, name='buscar_item'),
	path('next/', views.search_next, name='next'),
	path('page/',views.get_page, name='page'),
	path('link/',views.get_page_link, name='link'),
	path('paginacao/<int:start_id>/', views.paginacao, name='paginacao')
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)