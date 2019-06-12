# -*- coding: utf-8 -*-
import os
class Synthesizer:			

	def synthesizer(self, arg):
		inicio = "espeak -vpt -k 20 '"
		comand = "' -w "
		path = "/home/infsolution/Documentos/IFPI/TCC-ARQUIVOS/projeto/visio/media/audiosycn.wav"
		os.system(inicio+arg+comand+path)
		return path
		
