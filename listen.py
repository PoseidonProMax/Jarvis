import speech_recognition as sr

r = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("\nListening...")
        audio = r.listen(source)

    try:

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except:

        print("Could not understand")

        return ""