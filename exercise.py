from gtts import gTTS
from playsoud import playsound

class Exercise:
    def __init__(self, type):
        self.type = type ##운동종목 정수로 판별
        self.count = 0
        self.status = True

    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound(filename)
        return








