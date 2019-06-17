 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import requests
from .page import Page
from . import synthesizer
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
			return render(request,'makevisio/content.html',{'values':response.json()['items']})
	else:
		return render(request,'makevisio/content.html',{"error":"Sem resposta."})



def get_page(request,url):
	page = Page(url)
	#print(page.dic_page)
	return render(request,'makevisio/page.html',{'page':page.list_page,})

def get_page_(request):
	if request.POST.get('link'):
		page = Page(request.POST.get('link'))
		return render(request,'makevisio/page.html',{'page':page.list_page,})


def create_audio_desc(response_json):
	list_search=[]
	synt = Synthesizer()
	for link in response_json:
		link_atr = LinkAtribut(link=link.link, displayLink=link.displayLink, 
			displayLink_audio=synt.synthesizer(link.displayLink), displayLink_id=create_id(link.displayLink),
			title=link.title, title_audio=synt.synthesizer(link.title), title_id=create_id(link.title),
			snippet=lik.snippet, snippet_audio=synt.synthesizer(link.snippet), snippet_id=create_id(link.snippet))

def create_id(value):
	return 'oi'
