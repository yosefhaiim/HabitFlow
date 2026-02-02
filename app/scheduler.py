from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.database import db


def check_reminders():
    now = datetime.utcnow().strftime("%H:%M")

    habits = db.habits.find({
        "reminder_enabled": True,
        "reminder_time": now
    })

    for habit in habits:
        user = db.users.find_one({"_id": habit["user_id"]})
        if user:
            print(
                f"[REMINDER] Email to {user['email']} – "
                f"Time to work on habit: {habit['title']}"
            )


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_reminders, "interval", minutes=1)
    scheduler.start()
