# Phase 3 Stable Build
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['ALSA_CARD'] = '0'

import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)

def listen():

    try:

        with mic as source:

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        command = r.recognize_google(audio).lower()

        print(f"You said: {command}")

        return command

    except:
        return ""