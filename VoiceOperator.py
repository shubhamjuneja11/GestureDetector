import speech_recognition as sr
import subprocess
import sys
import platform
import os
import webbrowser as wb
import pyttsx
from DisplayText import DisplayText

class VoiceOperator:
	def __init__(self):
		self.r = sr.Recognizer()
		self.defaultPath='/home/shubhamjuneja11/GestureDetector/Test'
		self.displayText=DisplayText()

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
			displayText.display("Creating Folder")
			self.CreateFolder(keyWords[2])
		elif(keyWords[0]=='google'):

			self.GoogleIt(keyWords[1])
		elif(keyWords[0]=='hello'):
			self.PlayMusic()

	def OpenFolder(self,path):
		 #Only for linux
		 displayText.display("Opening Window")
		 subprocess.Popen(["xdg-open", self.defaultPath+path])

	def CreateFolder(self,folderName):
		try:
			displayText.display("Creating Folder"+folderName)
			directory = self.defaultPath+folderName
			if not os.path.exists(directory):
				os.makedirs(directory)
		except OSError as e:
			print('Folder exist')

	def GoogleIt(self,searchQuery):
		displayText.display("Google - "+searchQuery)
		url = 'https://www.google.co.in/search?&q='
		chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
		webbrowser.get(using='google-chrome').open(url+searchQuery)

	'''def PlayMusic(self,music):
		path=self.defaultPath+music
		os.system('rhythmbox '+path)'''

	def PlayMusic(self):
		engine = pyttsx.init()
		engine.say("How are you feeling today?")
		print("Currently I support happy, sad, and angry as emotions!")

		#audio = self.r.listen(source,timeout=1,phrase_time_limit=5)
		try:
				#detectedText = self.r.recognize_google(audio)
				#print(detectedText)

				keywords = []
				keywords.append("happy")
				if(keywords[0]=="happy"):
					wb.open("https://www.youtube.com/watch?v=pBkHHoOIIn8&list=PLinS5uF49IBo8HLKBDAjQaeiN4TjHi75Q")
				elif(keyWords[0]=='sad'):
					wb.open("https://www.youtube.com/watch?v=RgKAFK5djSk&list=PL5D7fjEEs5yflZzSZAhxfgQmN6C_6UJ1W")
				elif(keyWords[0]=="angry"):
					wb.open("https://www.youtube.com/watch?v=A6APxbBYnoo&list=PL36D9BFA8F76A2645")


		except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))
