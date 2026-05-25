import os
import datetime
from speak import speak
import random
responses = [
    "Yes?",
    "I'm listening.",
    "What do you need?",
    "Tell me.",
    "Ready."
]

def execute(command):

    if "firefox" in command or "fire fox" in command:
        speak("Opening Firefox")
        os.system("firefox")

    elif "spotify" in command:
        speak("Opening Spotify")
        os.system("spotify")

    elif "youtube" in command or "you tube" in command:
        speak("Opening YouTube")
        os.system("firefox https://youtube.com")

    elif "google" in command:
        speak("Opening Google")
        os.system("firefox https://google.com")

    elif "time" in command:
        current = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "exit" in command:
        speak("Goodbye")
        return False

    else:
        speak("Command not recognized")

    return True