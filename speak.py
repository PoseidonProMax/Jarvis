import pyttsx3
import threading

engine = pyttsx3.init()

engine.setProperty('rate', 170)

def speak_text(text):

    engine.say(text)
    engine.runAndWait()

def speak(text):

    thread = threading.Thread(target=speak_text, args=(text,))
    thread.start()