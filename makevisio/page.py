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
		self.dic_path = {}
		self.load_data()

	def __str__(self):
		return self.page.title.string

	def get_page(self, url):
		try:
			r = requests.get(url)
		except Exception as e:
			print(e)
			return e
		page = BeautifulSoup(r.text.encode('utf-8').decode('utf-8', ''), 'html.parser')
		return page

	def add_element(self, key, value):
		self.dic_page[key]=value

	def add_title(self):
		if self.page.title:
			synt = Synthesizer()
			atr = Atribut(name='titulo', name_audio=synt.synthesizer('título'), id_name='titulo_audio'
				, description=self.page.title.string, path_audio=synt.synthesizer(self.page.title.string),
				id_description='titulo_desc')
			self.list_page.append(atr)
			'''self.add_element('título',self.page.title.string)
												synt = Synthesizer()
												self.dic_path['titulo']=synt.synthesizer(self.page.title.string)
									'''
	
	def add_h1(self):
		if self.page.h1:
			self.add_element('título da página', self.page.h1.string)	
	def add_content(self):
		p_dic={}
		if self.page.body.div:
			content=self.page.body.findAll('p')
			for p in range(len(content)):
				p_dic[p]=content[p].string
			self.add_element('conteúdo', p_dic)
	def add_link(self):
		link_dic={}
		if self.page.findAll('a'):
			links = self.page.body.findAll('a',{"href":re.compile("http?://(.*?)")})
			for link in links:
				link_dic[link.string]=link['href']
			self.add_element('links', link_dic)
	
	def add_form(self):
		if self.page.form:
			self.add_element('formulário', self.page.form)
	def load_data(self):
		#self.add_link()
		self.add_title()
		#self.add_h1()
		#self.add_content()
		#self.add_form()
		



