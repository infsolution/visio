 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import requests
import json
def index(request):
	return render(request, 'makevisio/index.html')

def search_google(request):
	if request.GET.get('busca'):
		url = 'https://www.googleapis.com/customsearch/v1'
		params = {"key":"AIzaSyB_Uc-MGGJuKcZHGTU29UtbeL_V9H90Dgw", 
			"cx":"000119369848927943107:8no6nr65eju", 
			"q":request.GET.get('busca').encode('utf-8')}
		try:
			response = requests.get(url, params)
			#print(response.json())
		except Exception as e:
			print(e)
			return render(request,'makevisio/content.html',{"error":e})
		return render(request,'makevisio/content.html',{'values':response.json()['items']})
	else:
		return render(request,'makevisio/content.html',{"error":"Sem resposta."})



def get_page(request):
	if request.method == 'POST':
		return render(request,'makevisio/page.html',{'link':request.POST['link']})