from bs4 import BeautifulSoup
import requests
import re
class Page:
	def __init__(self, url):
		self.url = url

	def __str__(self):
		return self.get_page()

	def get_page(self):
		try:
			r = requests.get(self.url)
		except Exception as e:
			print("Connection error in "+self.url)
			return None
		return r.text

	def get_body(self):
		pattern = re.compile(r'>(.*?)</body>')
		return pattern.findall(self.get_page())
	def  get_title(self):
		pattern = re.compile(r'<title>(.*?)</title>')
		return pattern.findall(self.get_page())
	def get_title_h1(self):
		pattern = re.compile(r'>(.*?)</h1>')
		return pattern.findall(self.get_page())
	def get_topics(self):
		pattern = re.compile(r'<h4>(.*?)</h4>')
		return pattern.findall(self.get_page())
	def get_links(self):
		pattern = re.compile(r'href="(.*?)"')
		return pattern.findall(self.get_page())
	def links(self):
		pattern =re.compile(r'http?://')
		return pattern.findall(self.get_links()[0])
