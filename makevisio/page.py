# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
class Page:
	def __init__(self, url):
		self.page = self.get_page(url)
		self.title = self.page.title.string
		self.h1 = self.page.h1.string

	def __str__(self):
		return self.page.title.string

	def get_page(self, url):
		try:
			r = urlopen(url).read().decode('utf-8')
		except Exception as e:
			print(e)
			return e
		page = BeautifulSoup(r,'html.parser')
		return page

