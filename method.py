from gtts import gTTS
from playsound import playsound
import time
import os.path
from os import path


def speak(text):
    tts = gTTS(text=text, lang='en')

    filename = 'mp3_file/' + text + '.mp3'
    if not (path.exists(filename)):
        tts.save(filename)
    playsound(filename)
    return True


def time_count(second):
    for i in range(second):
        print(second-i)
        time.sleep(1)
    return True