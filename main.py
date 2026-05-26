import random
from listen import listen
from commands import execute, responses

print("Jarvis Assistant Started...")

running = True

while running:

    wake_command = listen()

    if "jarvis" in wake_command:

        response = random.choice(responses)
        print("Activated")

        command = listen()

        if command:
            running = execute(command)