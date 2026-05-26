import speech_recognition as sr

r = sr.Recognizer()

# Calibrate microphone once
with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)

def listen():

    with sr.Microphone() as source:
        r.pause_threshold = 1

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=6
        )

    try:

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except:

        return ""