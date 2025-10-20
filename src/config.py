import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DEFAULT_CLASS = os.getenv("DEFAULT_CLASS", "3O")
