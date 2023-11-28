from gtts import gTTS
from playsound import playsound
import time
import os.path
from os import path
# from interface import time_show


class Exercise:
    def __init__(self, type):
        self.type = type
        self.count = -1
        self.status = True

    def speak(self, text):
        tts = gTTS(text=text, lang='en')

        filename = text+'.mp3'
        if not(path.exists(filename)):
            tts.save(filename)
        playsound(filename)
        return

    def time_count(self, second):
        for i in range(second):
            print(second-i)
            time.sleep(1)
        return True








