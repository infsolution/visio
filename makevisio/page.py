# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests
import re
class Page:
	def __init__(self, url):
		self.page = self.get_page(url)
		self.dic_page = {}
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
			self.add_element('title',self.page.title.string)
	
	def add_h1(self):
		if self.page.h1:
			self.add_element('titulo da página', self.page.h1.string)	
	def add_content(self):
		if self.page.findAll('content'):
			self.add_element('content',self.page.findAll('content'))
	def add_link(self):
		link_dic={}
		if self.page.findAll('a'):
			links = self.page.body.findAll('a',{"href":re.compile("http?://(.*?)")})
			for link in links:
				link_dic[link.string]=link['href']
			self.add_element('links', link_dic)
	
	def load_data(self):
		self.add_title()
		self.add_h1()
		self.add_content()
		self.add_link()