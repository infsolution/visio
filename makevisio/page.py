# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
class Page:
	def __init__(self, url):
		self.page = self.get_page(url)
		self.title = self.page.title.string
		self.links = self.page.findAll(href=True)
		self.h1 = self.page.h1.string

	#def __str__(self):
	#	return self.page.title.string

	def get_page(self, url):
		try:
			r = requests.get(url)
		except Exception as e:
			print(e)
			return e
		page = BeautifulSoup(r.text.encode('utf-8').decode('utf-8', ''), 'html.parser')
		return page

