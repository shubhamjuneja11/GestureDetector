from VoiceOperator import VoiceOperator
from GestureDetector import GestureDetector
if __name__ == "__main__":
    #Choose whichever, haven't checked running simultaneously and not ready to take this risk at 1 a.m.
    '''voiceOperator = VoiceOperator()
    voiceOperator.StartAudioController()'''
    gestureDetector = GestureDetector()
    gestureDetector.StartDetection()
