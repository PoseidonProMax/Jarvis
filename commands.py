# Phase 3 Stable Build
import os
from datetime import datetime
from speak import speak

responses = [
    "At your service.",
    "I'm here.",
    "Go ahead.",
    "What can I do for you?",
    "Yes sir.",
    "Ready for your command."
]

def execute(command):

    # Firefox
    if "firefox" in command or "fire fox" in command:

        os.system("firefox &")
        speak("Opening Firefox")

    # Spotify
    elif "spotify" in command:

        os.system("spotify &")
        speak("Opening Spotify")

    # YouTube
    elif "youtube" in command or "you tube" in command:

        os.system("firefox https://youtube.com &")
        speak("Opening YouTube")

    # Google
    elif "google" in command:

        os.system("firefox https://google.com &")
        speak("Opening Google")

    # Time
    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(current_time)

    # Date
    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        speak(today)

    # Exit
    elif "exit" in command:

        speak("Goodbye")

        return False

    else:

        speak("Command not recognized")

    return True