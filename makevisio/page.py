# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .synthesizer import *
from . models import *
import json
import requests
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
				id_description=self.replace_all(word), atributo=atr)
			item.save()
			self.list_page.append(atr)
		else:
			for p in content_alt:
				if p.get_text() != None and len(p.get_text()) > 60:
					p_list.append(p.get_text())
			word = self.add_item(p_list)
			synt = Synthesizer()
			atr = Atribut(name='conteudo', name_audio=synt.synthesizer('conteúdo'), id_name='conteudo_audio')
			atr.save()
			item = Item(description=word, path_audio=synt.synthesizer(word),
				id_description=self.replace_all(word), atributo=atr)
			item.save()
			self.list_page.append(atr)

	def add_link(self):
		links = self.page.body.find_all("a",href=True)
		if links:
			synt = Synthesizer()
			for link in links:
				if link.get_text():
					atr = Atribut(name=link.get_text(), name_audio=synt.synthesizer(link.get_text()), id_name=self.replace_all(link.get_text()))
					atr.save()
					item = Item(description=link.get("href"), path_audio=synt.synthesizer(link.get("href")), id_description=self.replace_all(link.get("href")),
					opt_link=link.get("href"), atributo=atr)
					item.save()
					self.list_links.append(atr)

	def add_form(self):
		if self.page.form:
			self.add_element('formulário', self.page.form)

	def load_data(self):
		self.add_link()
		self.add_title()
		#self.add_h1()
		self.add_content()
		#self.add_form()

	def replace_all(self, word):
		for w in [" ","/","|","'","_","-","%","*","&","#","@","(",")","+","=","!","?",",",".",":",";","ã","Â","Ã","ã","ú","Ú","ó","Ó"]:
			word = word.replace(w, "")
		return word[2:10]+'_desc'