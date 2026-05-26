import speech_recognition as sr

r = sr.Recognizer()

# Calibrate microphone once
with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)

def listen(text=""):

    with sr.Microphone() as source:

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=4
        )

    try:

        command = r.recognize_google(audio).lower()

        if text:
            print(text)

        print("You said:", command)

        return command

    except:

        return ""