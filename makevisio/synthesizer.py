# -*- coding: utf-8 -*-
import os
class Synthesizer:			

	def synthesizer(self, arg):
		inicio = "espeak -vpt -k 20 '"
		comand = "' -w "
		path = "/home/cicero/Documentos/IFPI/TCC/visio/media/"
		name = self.replace_all(arg[0:20])
		exte =".wav"
		os.system(inicio+arg+comand+path+name+exte)
		return "media/"+name+exte
		

	def replace_all(self, word):
		for w in [" ","/","|","'","_","-","%","*","&","#","@","(",")","+","=","!","?",",",".",":",";"]:
			word = word.replace(w, "")
		return word