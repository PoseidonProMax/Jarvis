import pyttsx3

engine = pyttsx3.init()

# Slower speaking speed
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()