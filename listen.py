import speech_recognition as sr
from speak import speak

r = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("\nListening...")
        speak("Listening")

        audio = r.listen(source)

    try:

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except:

        print("Could not understand")
        speak("I could not understand")

        return ""