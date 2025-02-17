from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "29171167"))
    API_HASH = getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "https://github.com/ak4422920/Surf-TG").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://tg:tg@cluster0.fekvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002475275261,-1002184877471,-1002333030990,-1002295131184,-1002435507517").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "ak")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "cine")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "cine")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
