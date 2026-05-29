import json
import threading
import os

from datetime import datetime, timedelta
from speak import speak

active_timers = []


def load_reminders():

    try:

        with open("reminders.json", "r") as f:

            return json.load(f)

    except:

        return []


def save_reminders(reminders):

    with open("reminders.json", "w") as f:

        json.dump(reminders, f, indent=4)


def set_reminder(message, seconds):

    reminders = load_reminders()

    reminder_id = (
        max([r["id"] for r in reminders], default=0)
        + 1
    )

    due_time = datetime.now() + timedelta(
        seconds=seconds
    )

    reminders.append({
        "id": reminder_id,
        "task": message,
        "due": due_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    })

    save_reminders(reminders)

    def reminder():

        print("REMINDER FIRED")

        os.system(
            f'notify-send "Jarvis Reminder" "{message}"'
        )

        speak(message)

        reminders = load_reminders()

        reminders = [
            r for r in reminders
            if r["id"] != reminder_id
        ]

        save_reminders(reminders)

    timer = threading.Timer(
        seconds,
        reminder
    )

    timer.start()

    active_timers.append(timer)


def show_reminders():

    reminders = load_reminders()

    if not reminders:

        print("\nNo reminders found.\n")

        return

    print("\nPending Reminders:\n")

    for reminder in reminders:

        print(
            f'{reminder["id"]}. '
            f'{reminder["task"]} '
            f'-> {reminder["due"]}'
        )


def cancel_reminder(reminder_id):

    reminders = load_reminders()

    reminders = [
        r for r in reminders
        if r["id"] != reminder_id
    ]

    save_reminders(reminders)


def cancel_all_reminders():

    save_reminders([])


def restore_reminders():

    reminders = load_reminders()

    now = datetime.now()

    for reminder in reminders:

        due = datetime.strptime(
            reminder["due"],
            "%Y-%m-%d %H:%M:%S"
        )

        seconds = (
            due - now
        ).total_seconds()

        if seconds > 0:

            def reminder_callback(
                message=reminder["task"],
                reminder_id=reminder["id"]
            ):

                print("REMINDER FIRED")

                os.system(
                    f'notify-send "Jarvis Reminder" "{message}"'
                )

                speak(message)

                reminders = load_reminders()

                reminders = [
                    r for r in reminders
                    if r["id"] != reminder_id
                ]

                save_reminders(reminders)

            timer = threading.Timer(
                seconds,
                reminder_callback
            )

            timer.start()

            active_timers.append(timer)