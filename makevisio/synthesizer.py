# -*- coding: utf-8 -*-
import os
class Synthesizer:			

	def synthesizer(self, arg):
		arg = arg.strip()
		inicio = "espeak -vpt -k 20 '"
		comand = "' -w "
		#path = "/var/www/html/visio/media/"
		path = "/home/cicero/Documentos/IFPI/TCC/visio/media/"
		if len(arg) > 10:
			name = self.replace_all(arg[10:29])
		else:
			name = self.replace_all(arg[0:10])
		exte =".wav"
		os.system(inicio+arg+comand+path+name+exte)
		#os.system(u' '.join((inicio,arg,comand,path,name,exte)).encode('utf-8'))
		return "media/"+name+exte
		

	def replace_all(self, word):
		for w in [" ","/","|","'","_","-","%","*","&","#","@","(",")","+","=","!","?",",",".",":",";","ã","Â","Ã","ã","ú","Ú","ó","Ó"]:
			word = word.replace(w, "")
		return word



#[]