import discord
from discord import app_commands
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
    try:
        await bot.tree.sync()
        print("Slash commands synced")
    except Exception as e:
        print(f"Warning: failed to sync commands: {e}")


@bot.tree.command(name="rozvrh", description="Zobraz rozvrh pro zadanou třídu")
async def rozvrh(interaction: discord.Interaction, trida: str = DEFAULT_CLASS):
    await interaction.response.defer()
    data = get_timetable(trida)
    text = []
    for den, hodiny in data.items():
        text.append(f"**{den}**")
        for h in hodiny:
            text.append(f"{h['hour']}. {h['subject']} ({h['teacher']}) – {h['room']}")
        text.append("")
    await interaction.followup.send("\n".join(text))


@bot.tree.command(name="setup", description="Nastav svoji třídu pro notifikace")
async def setup(interaction: discord.Interaction, trida: str):
    set_user(interaction.user.id, trida)
    await interaction.response.send_message(f"✅ Nastavil jsi si třídu **{trida}**. Každý den ve 22:00 ti pošlu rozvrh do DM!")


if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("ERROR: DISCORD_TOKEN is not set. Please define it in your environment or .env file.")
        raise SystemExit(1)
    try:
        bot.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        print("ERROR: Login failed — the provided DISCORD_TOKEN is invalid or revoked.\nPlease check that you pasted the bot token from the Discord Developer Portal (Bot section), or regenerate the token and update your .env file.")
        raise SystemExit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error while starting the bot: {e}")
        raise
