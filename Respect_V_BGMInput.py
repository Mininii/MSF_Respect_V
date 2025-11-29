from eudplib import *
import math
import os

#Laptop : 'C:\\Users\\whatd\\Desktop\\Stormcoast Fortress\\ScmDraft 2\\MapSource\\MEME_EUD_Project\\'
#Desktop : 'C:\\Users\\USER\\Documents\\MapSource\\MEME_EUD_Project'

def Exec_OggFile():
	filenames = os.listdir("C:/euddraft0.9.2.0/Respect_V_BGM/")
	for filename in filenames:
		ext = os.path.splitext(filename)[-1]
		if ext == '.ogg': 
			print(filename)
			MPQAddFile('staredit\\wav\\'+filename, open('C:/euddraft0.9.2.0/Respect_V_BGM/'+filename, 'rb').read())
		if ext == '.wav': 
			print(filename)
			MPQAddFile('staredit\\wav\\'+filename, open('C:/euddraft0.9.2.0/Respect_V_BGM/'+filename, 'rb').read())
			
