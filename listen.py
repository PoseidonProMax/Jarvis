import speech_recognition as sr
from speak import speak

r = sr.Recognizer()

# Calibrate microphone once
with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)

def listen():

    with sr.Microphone() as source:

        print("\nListening...")
        speak("Listening")

        audio = r.listen(source, phrase_time_limit=5)

    try:

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except:

        print("Could not understand")
        speak("I could not understand")

        return ""