import os
from dotenv import load_dotenv
from db import create_admin

load_dotenv()
telegram_user_id = os.getenv("BOT_ABSOLUTE_ADMIN")
(create_admin(telegram_user_id=telegram_user_id,status="absolute_admin"))