import random
from listen import listen
from commands import responses
from brain import think
from speak import speak

print("Jarvis online...\n")
print("Waiting wake word...")

running = True

while running:

    wake_command = listen()

    if "jarvis" in wake_command:

        print("\nActivated")

        response = random.choice(responses)
        speak(response)

        print("Awaiting command...")

        command = listen()

        if command:

            print(f"\nCommand: {command}")

            running = think(command)

            if running:
                print("\nWaiting wake word...")