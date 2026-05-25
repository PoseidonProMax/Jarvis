import speech_recognition as sr

r = sr.Recognizer()

# Calibrate microphone once
with sr.Microphone() as source:
    print("Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=1)

def listen(text="Waiting..."):

    with sr.Microphone() as source:

        print(text)

        audio = r.listen(
    source,
    timeout=2,
    phrase_time_limit=3
)

    try:

        command = r.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except:

        print("Could not understand")

        return ""