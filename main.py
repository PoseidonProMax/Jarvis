import time
import random
from listen import listen
from commands import execute, responses
from speak import speak

print("Jarvis Assistant Started...")
speak("Jarvis Assistant Activated")

running = True

while running:

    wake_command = listen("Waiting...")

    if "jarvis" in wake_command:

        response = random.choice(responses)
        speak(response)

        command = listen("Command...")

        if command:
            running = execute(command)

    time.sleep(1)