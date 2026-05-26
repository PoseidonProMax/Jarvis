# Phase 3 Stable Build
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 175)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):

    engine.stop()

    engine.say(text)

    engine.runAndWait()