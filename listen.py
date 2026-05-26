import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['ALSA_CARD'] = '0'

import speech_recognition as sr

r = sr.Recognizer()

def listen():

    try:

        with sr.Microphone() as source:

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        command = r.recognize_google(audio).lower()

        print(f"You said: {command}")

        return command

    except:
        return ""