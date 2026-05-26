import random
from listen import listen
from commands import execute, responses
from speak import speak

print("Jarvis Assistant Started...")

running = True

while running:

    wake_command = listen()

    if "jarvis" in wake_command:

        print("Activated")

        response = random.choice(responses)
        speak(response)

        command = listen("Command...")

        if command:
            running = execute(command)