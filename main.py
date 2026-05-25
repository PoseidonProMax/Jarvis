import time
from listen import listen
from commands import execute

print("Jarvis Assistant Started...")

running = True

while running:

    command = listen()

    if command:
        running = execute(command)

    time.sleep(1)