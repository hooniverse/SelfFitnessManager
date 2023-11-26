from gtts import gTTS
from playsound import playsound
import time
from interface import time_show


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

    def time_count(self, minute, second):
        second += minute*60
        for i in second:
            time_show(second-i)
            time.sleep(1)
        return True

    def exercise(self):
        return







