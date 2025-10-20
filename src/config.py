import os
from dotenv import load_dotenv

load_dotenv()

# Read token and normalize it (strip whitespace, remove optional 'Bot ' prefix)
_raw_token = os.getenv("DISCORD_TOKEN")
if _raw_token:
	_raw_token = _raw_token.strip()
	if _raw_token.startswith("Bot "):
		# Some people copy the token including the 'Bot ' prefix; remove it
		_raw_token = _raw_token.split(" ", 1)[1]

DISCORD_TOKEN = _raw_token
DEFAULT_CLASS = os.getenv("DEFAULT_CLASS", "3O")
