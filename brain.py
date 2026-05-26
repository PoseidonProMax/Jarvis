from commands import execute
from speak import speak

def think(command):

    system_commands = [
        "spotify",
        "firefox",
        "youtube",
        "google",
        "time",
        "date",
        "exit"
    ]

    for word in system_commands:

        if word in command:
            return execute(command)

    if "how are you" in command:

        speak("I am functioning perfectly.")

    elif "who made you" in command:

        speak("Abhinav created me.")

    elif "your name" in command:

        speak("I am Jarvis.")

    elif "hello" in command:

        speak("Hello Abhinav.")

    else:

        speak("I don't know that command yet.")

    return True