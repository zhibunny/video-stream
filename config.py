import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Dame_De_CoeuR")
ALIVE_NAME = getenv("ALIVE_NAME", "BUNNY")
BOT_USERNAME = getenv("BOT_USERNAME", "Ashique_Zhi_vcBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ashique_Zhi_Vc")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BUNNY_ZONE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BUNNY_ZONE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/e09ffea5c0041bc2635cb.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e09ffea5c0041bc2635cb.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/e09ffea5c0041bc2635cb.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/e09ffea5c0041bc2635cb.png")
