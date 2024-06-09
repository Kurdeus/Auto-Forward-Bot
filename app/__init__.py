import os
os.system("pip install -r ./requirements.txt")


from pyrogram import Client, enums
from asyncio import get_event_loop
import os
from dotenv import load_dotenv


def getConfig(name: str):
    return os.environ[name]


load_dotenv('config.env')



MY_CHANNEL_ID = int(getConfig("MY_CHANNEL_ID"))
TARGET_CHANNEL_ID = int(getConfig("TARGET_CHANNEL_ID"))
TELEGRAM_API = int(getConfig("TELEGRAM_API"))
TELEGRAM_HASH = getConfig("TELEGRAM_HASH")


main_loop = get_event_loop()
bot = Client(name="bot", api_id=int(TELEGRAM_API), api_hash=TELEGRAM_HASH, parse_mode=enums.ParseMode.HTML)

