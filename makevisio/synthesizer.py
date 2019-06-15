# -*- coding: utf-8 -*-
import os
class Synthesizer:			

	def synthesizer(self, arg):
		inicio = "espeak -vpt -k 20 '"
		comand = "' -w "
		path = "/home/infsolution/Documentos/IFPI/TCC-ARQUIVOS/projeto/visio/media/"
		name = arg.replace(" ","_")
		exte =".wav"
		os.system(inicio+arg+comand+path+name+exte)
		return "media/"+name+exte
		
