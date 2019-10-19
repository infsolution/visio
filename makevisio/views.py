 # -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render, redirect
from datetime import datetime
from .synthesizer import *
from .models import *
from .page import Page
import requests
import json

def index(request):
	return render(request, 'makevisio/index.html')

def search_google(request):
	if request.POST.get('busca'):
		if 'http' in request.POST.get('busca') or 'https' in request.POST.get('busca'):
			return get_page(request, request.POST.get('busca'))
		else:
			url = 'https://www.googleapis.com/customsearch/v1'
			params = {"key":"AIzaSyB_Uc-MGGJuKcZHGTU29UtbeL_V9H90Dgw",
				"cx":"000119369848927943107:8no6nr65eju",
				"q":request.POST.get('busca')}
			try:
				response = requests.get(url, params)
			except Exception as e:
				print("Error: "+e)
				return render(request,'makevisio/content.html',{"error":e})
			return render(request,'makevisio/content.html',{'values':create_audio_desc(response.json()['items']),})
	else:
		return render(request,'makevisio/content.html',{"error":"Sem resposta."})

def get_page(request,url):
	page = Page(url)
	return render(request,'makevisio/page.html',{'page':page.list_page,'page_links':page.list_links,})

def get_page_link(request):
	if request.POST.get('link'):
		page = Page(requests.POST.get('link'))
		return render(request,'makevisio/page.html',{'page':page.list_page,})


def create_audio_desc(response_json):
	#print(response_json)
	list_search=[]
	synt = Synthesizer()
	for link in response_json:
		link_atr = LinkAtribut(link=link['link'], displayLink=link['displayLink'],
			displayLink_audio=synt.synthesizer(link['displayLink']), displayLink_id=create_id(link['displayLink']),
			title=link['title'], title_audio=synt.synthesizer(link['title']), title_id=create_id(link['title']),
			snippet=link['snippet'], snippet_audio=synt.synthesizer(link['snippet']), snippet_id=create_id(link['snippet']))
		list_search.append(link_atr)
	return list_search

def create_id(value):
	value_id = ''
	for w in [" ","/","|","'","_","-","%","*","&","#","@","(",")","+","=","!","?",",",".",":",";"]:
			value = value.replace(w, "")
	value_id = value[0:10]
	value_id += datetime.now().strftime("%d-%b-%Y-%H:%M:%S.%f")
	return value_id

def paginacao(request, start_id):
	ITEMS_PER_PAGE = 5
	items = Atribut.objects.filter(id__gte=start_id)
	paginator = Paginator(items, ITEMS_PER_PAGE)
	page = request.GET.get('page',1)
	print(page)
	try:
		items_page = paginator.get_page(page)
	except InvalidPage:
		items_page = paginator.get_page(1)
	return render(request, 'makevisio/page_links.html',{'page_links':items_page, 'page':[]})
