# -*- coding: utf-8 -*-
import os
class Synthesizer:
	def __init__(self, arg):
		#os.system("espeak -vpt -k 20 arg -w /audiotmp/audio.wav")
		os.system("espeak -vpt -k 20 "+arg+" -w /home/cicero/Documentos/IFPI/TCC/visio/static/audio/audio.wav")	
		
