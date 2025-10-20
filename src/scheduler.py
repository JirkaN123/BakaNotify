import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import get_timetable
from db import get_user
from discord.ext import commands

scheduler = AsyncIOScheduler()

async def send_daily(bot: commands.Bot):
    """Posílá rozvrh v 22:00"""
    for user in bot.users:
        info = get_user(user.id)
        if info and info[1] == 1:
            class_name = info[0]
            timetable = get_timetable(class_name)
            msg = format_timetable(timetable)
            try:
                await user.send(f"📅 **Rozvrh pro {class_name} na zítřek:**\n\n{msg}")
            except Exception as e:
                print(f"❌ Nelze poslat DM uživateli {user}: {e}")

def format_timetable(data):
    text = []
    for den, hodiny in data.items():
        text.append(f"**{den}**")
        for h in hodiny:
            text.append(f"{h['hour']}. {h['subject']} ({h['teacher']}) – {h['room']}")
        text.append("")
    return "\n".join(text)

def start(bot: commands.Bot):
    scheduler.add_job(send_daily, "cron", hour=22, minute=0, args=[bot])
    scheduler.start()
