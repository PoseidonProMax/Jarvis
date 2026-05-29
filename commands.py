import os
from datetime import datetime
from speak import speak
from pathlib import Path
from reminders import set_reminder

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

    # Dynamic App Launcher
    elif "open" in command:

        app = command.replace("open", "").strip()

        app_commands = {
            "discord": "discord",
            "vscode": "code",
            "vs code": "code",
            "files": "nautilus",
            "terminal": "gnome-terminal",
            "spotify": "spotify",
            "firefox": "firefox"
        }

        if app in app_commands:

            os.system(f"{app_commands[app]} &")

            speak(f"Opening {app}")

        else:

            speak("Application not found")

    # YouTube
    elif "youtube" in command or "you tube" in command:

        os.system("firefox https://youtube.com &")
        speak("Opening YouTube")

    # Google
    elif "google" in command:

        os.system("firefox https://google.com &")
        speak("Opening Google")
            # Volume Up
    elif "volume up" in command:

        os.system("amixer -D pulse sset Master 10%+")

        speak("Volume increased")

    # Volume Down
    elif "volume down" in command:

        os.system("amixer -D pulse sset Master 10%-")

        speak("Volume decreased")

        # Unmute
    elif command == "unmute":

        os.system("amixer -D pulse sset Master unmute > /dev/null 2>&1")

        speak("Unmuted")

    # Mute
    elif command == "mute":

        os.system("amixer -D pulse sset Master mute > /dev/null 2>&1")

        speak("Muted")

    # Screenshot
    elif "screenshot" in command:

        os.system("/home/abhi/Applications/Flameshot-13.3.0.x86_64.AppImage gui &")

        speak("Taking screenshot")

    # Time
    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(current_time)

    # Date
    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        speak(today)
    # Pause Music
    elif "pause music" in command:

        os.system("playerctl pause")

        speak("Music paused")

    # Play Music
    elif "play music" in command:

        os.system("playerctl play")

        speak("Playing music")

    # Next Song
    elif "next song" in command:

        os.system("playerctl next")

        speak("Next song")

    # Previous Song
    elif "previous song" in command:

        os.system("playerctl previous")

        speak("Previous song")
     # Take Note
    elif command.startswith("take note"):

        note = command.replace("take note", "").strip()

        with open("notes.txt", "a") as f:
            f.write(note + "\n")

        speak("Note saved")

    # Show Notes
    elif command == "show notes":

        try:

            with open("notes.txt", "r") as f:

                notes = f.read()

            if notes.strip():

                speak("Here are your notes")

                print("\nNotes:\n")
                print(notes)

            else:

                speak("No notes found")

        except FileNotFoundError:

            speak("No notes found")

    # Clear Notes
    elif command == "clear notes":

        open("notes.txt", "w").close()

        speak("Notes cleared")
     # Reminder
     
    elif command.startswith("remind me to"):

        try:

            reminder_text = command.replace(
                "remind me to",
                ""
            ).strip()

            if " in " not in reminder_text:

                speak("Please specify a time")

                return True

            task, duration = reminder_text.rsplit(" in ", 1)

            seconds = 0

            if "minute" in duration:

                number = int(duration.split()[0])

                seconds = number * 60

            elif "hour" in duration:

                number = int(duration.split()[0])

                seconds = number * 3600

            elif "day" in duration:

                number = int(duration.split()[0])

                seconds = number * 86400

            else:

                speak("Unsupported time format")

                return True

            set_reminder(task, seconds)

            speak("Reminder saved")

        except:

            speak("Could not create reminder")
     # Desktop Notification
    elif command.startswith("notify"):

        message = command.replace("notify", "").strip()

        if message:

            os.system(f'notify-send "Jarvis" "{message}"')

            speak("Notification sent")

        else:

            speak("Please provide a notification message")
    # WiFi Status
    elif "wi-fi" in command:

        wifi = os.popen("nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d':' -f2").read().strip()

        if wifi:

            speak(f"Connected to {wifi}")

        else:

            speak("WiFi is disconnected")
    # Battery Status
    elif "battery" in command:

        battery = os.popen("upower -i $(upower -e | grep BAT) | grep percentage").read()

        battery = battery.split(":")[1].strip()

        speak(f"Battery is at {battery}")

    # Exit
    elif "exit" in command:

        speak("Goodbye")

        return False

    else:

        speak("Command not recognized")

    return True