import speech_recognition as sr
import subprocess
import sys
import platform
import os
import webbrowser

class VoiceOperator:
	def __init__(self):
		self.r = sr.Recognizer()
		self.defaultPath='/home/shubhamjuneja11/GestureDetector/Test'

	def StartAudioController(self):
		while(True):
			with sr.Microphone() as source:
				print("Say something!")
				audio = self.r.listen(source,timeout=1,phrase_time_limit=5)
			try:
				detectedText = self.r.recognize_google(audio)
				print(detectedText)
				self.CheckCommand(detectedText)
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

	def CheckCommand(self,detectedText):
		#Open Explorer
		keyWords = detectedText.split()
		if(keyWords[0] == 'open' and keyWords[1] == 'window'):
			self.OpenFolder('')
		elif(keyWords[0] == 'create' and keyWords[1]=='folder'):
			self.CreateFolder(keyWords[2])
		elif(keyWords[0]=='google'):
			self.GoogleIt(keyWords[1])

	def OpenFolder(self,path):
		 #Only for linux
		 subprocess.Popen(["xdg-open", self.defaultPath+path])

	def CreateFolder(self,folderName):
		try:
			directory = self.defaultPath+folderName
			if not os.path.exists(directory):
				os.makedirs(directory)
		except OSError as e:
			print('Folder exist')

	def GoogleIt(self,searchQuery):
		url = 'https://www.google.co.in/search?&q='
		chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
		webbrowser.get(using='google-chrome').open(url+searchQuery)
