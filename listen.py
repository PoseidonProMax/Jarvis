import os

# Hide Linux audio warning spam
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

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
                phrase_time_limit=10
            )

        command = r.recognize_google(audio)

        command = command.lower()

        print(f"You said: {command}")

        return command

    except sr.WaitTimeoutError:

        return ""

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        return ""

    except:

        return ""