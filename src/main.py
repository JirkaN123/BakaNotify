import discord
from discord.ext import commands
from config import DISCORD_TOKEN, DEFAULT_CLASS
from scraper import get_timetable
from db import init_db, set_user, get_user
from scheduler import start

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Přihlášen jako {bot.user}")
    init_db()
    start(bot)

@bot.add(description="Zobraz rozvrh pro zadanou třídu")
async def rozvrh(ctx, trida: str = DEFAULT_CLASS):
    await ctx.defer()
    data = get_timetable(trida)
    text = []
    for den, hodiny in data.items():
        text.append(f"**{den}**")
        for h in hodiny:
            text.append(f"{h['hour']}. {h['subject']} ({h['teacher']}) – {h['room']}")
        text.append("")
    await ctx.respond("\n".join(text))

@bot.slash_command(description="Nastav svoji třídu pro notifikace")
async def setup(ctx, trida: str):
    set_user(ctx.author.id, trida)
    await ctx.respond(f"✅ Nastavil jsi si třídu **{trida}**. Každý den ve 22:00 ti pošlu rozvrh do DM!")

bot.run(DISCORD_TOKEN)
