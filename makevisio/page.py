# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
#from background_task import background
from urllib.request import urlopen
from django.utils import timezone
from bs4 import BeautifulSoup
from .synthesizer import *
from . models import *
import requests
import json
import re
class Page:
	def __init__(self, url):
		self.page = self.get_page(url)
		self.dic_page = {}
		self.list_page = []
		self.list_links = []
		self.dic_path = {}
		if self.page:
			self.load_data()

	def __str__(self):
		return self.page.title.string

	def get_page(self, url):
		try:
			r = requests.get(url)
			r.encoding = r.apparent_encoding#new encoding
		except Exception as e:
			return None
		page = BeautifulSoup(r.text, features="html.parser")
		return page

	def add_element(self, key, value):
		self.dic_page[key]=value

	def add_title(self):
		if self.page.title:
			synt = Synthesizer()
			atr = Atribut(name='titulo', name_audio=synt.synthesizer('título'), id_name='titulo_audio')
			atr.save()
			item = Item(description=self.page.title.string, path_audio=synt.synthesizer(self.page.title.string),
				id_description='titulo_desc', atributo=atr)
			item.save()
			self.list_page.append(atr)
			#self.add_element('título',self.page.title.string)
			#synt = Synthesizer()
			#self.dic_path['titulo']=synt.synthesizer(self.page.title.string)

	'''def add_h1(self):
					if self.page.h1:
						self.add_element('título da página', self.page.h1.string)'''
	def add_item(self, items):
		string = ''
		for item in items:
			string += item
		return string

	def add_content(self):
		p_list=[]
		content = self.page.body.find_all("p")
		content_alt = self.page.find_all("p")
		if content:
			for p in content:
				if p.get_text() != None and len(p.get_text()) > 60:
					p_list.append(p.get_text())
			word = self.add_item(p_list)
			synt = Synthesizer()
			atr = Atribut(name='conteudo', name_audio=synt.synthesizer('conteúdo'), id_name='conteudo_audio')
			atr.save()
			item = Item(description=word, path_audio=synt.synthesizer(word),
				id_description='content_description', atributo=atr)
			item.save()
		else:
			for p in content_alt:
				if p.get_text() != None and len(p.get_text()) > 60:
					p_list.append(p.get_text())
			word = self.add_item(p_list)
			synt = Synthesizer()
			atr = Atribut(name='conteudo', name_audio=synt.synthesizer('conteúdo'), id_name='conteudo_audio')
			atr.save()
			item = Item(description=word, path_audio=synt.synthesizer(word),
				id_description='content_description', atributo=atr)
			item.save()
		self.list_page.append(atr)

	def add_link(self):
		links = self.page.body.find_all("a",href=True)
		lista = self.select_tag(links)
		self.links_synthesizer(lista)

	#@background(schedule=0)
	def links_synthesizer(self, links):
		links = self.clean_key(links)
		print(links)
		if links:
			synt = Synthesizer()
			for key, value in links.items():
				atr = Atribut(name=key, name_audio=synt.synthesizer(key), id_name=synt.replace_all(key))
				atr.save()
				item = Item(description=value, path_audio=synt.synthesizer(value), id_description=synt.replace_all(value),
				opt_link=value, atributo=atr)
				item.save()
				self.list_links.append(atr)
	def select_tag(self, links):
		links_dic = {}
		for link in links:
			if link.get_text() != "" and len(link.get_text()) > 5 and 'http' in link.get("href"):
				links_dic[link.get_text()]=link.get("href")
		return links_dic

	def add_form(self):
		if self.page.form:
			self.add_element('formulário', self.page.form)

	def load_data(self):
		self.add_title()
		self.add_content()
		#self.add_form()
		self.add_link()
	def clean_key(self, diction):
		dic = {}
		for key, value in diction.items():
			k = key.replace('\n','')
			k = k[0:30]
			dic[k] = value
		return dic