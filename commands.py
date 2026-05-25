import os
import datetime
from speak import speak
import random

responses = [
    "Yes?",
    "Hmm?",
    "Ready.",
]

def execute(command):

    # Firefox
    if "firefox" in command or "fire fox" in command:
        os.system("firefox")
        speak("Opening Firefox")

    # Spotify
    elif "spotify" in command:
        os.system("spotify")
        speak("Opening Spotify")

    # YouTube
    elif "youtube" in command or "you tube" in command:
        os.system("firefox https://youtube.com")
        speak("Opening YouTube")

    # Google
    elif "google" in command:
        os.system("firefox https://google.com")
        speak("Opening Google")

    # Time
    elif "time" in command:
        current = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current}")

    # Date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    # Exit
    elif "exit" in command:
        speak("Goodbye")
        return False

    # Unknown
    else:
        speak("Command not recognized")

    return True