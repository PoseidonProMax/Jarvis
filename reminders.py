import threading
import os
from speak import speak

def set_reminder(message, seconds):

    def reminder():

        os.system(f'notify-send "Jarvis Reminder" "{message}"')

        speak(message)

    timer = threading.Timer(seconds, reminder)

    timer.start()