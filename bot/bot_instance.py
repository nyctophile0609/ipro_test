import os
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

bot=Bot(
    token=os.getenv("INSTAGRAM_BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode="HTML")
)

