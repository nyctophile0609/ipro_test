from aiogram.exceptions  import TelegramNotFound,TelegramForbiddenError
from aiogram.enums.chat_member_status import ChatMemberStatus
from bot_instance import bot

from database.db import *
async def get_user_profile(user_id):
    try:
        chat = await bot.get_chat(user_id)
        if chat:
            return chat
        return False
    except Exception as e:
        return False


def format_the_username(username):
    if "https://t.me/"  in username or "@" not in username:
        ahah=username.split("https://t.me/")
        return "@"+ahah
    elif "@" in username:
        return username




async def is_bot_worthy(username):
    try:
        res=await bot.get_chat_member(username,bot.id)
        print(res.status)
        print(res.can_post_messages)
        print(res.can_delete_messages)
        if res.status==ChatMemberStatus.ADMINISTRATOR and res.can_delete_messages and res.can_post_messages!=False:

            return {"success":True}
        return {"success":False,"reason":1}

    except TelegramForbiddenError as e:
        return {"success":False,"reason":2}   
    except TelegramNotFound as e:
        return {"success":False,"reason":3} 
    except Exception as e:
        print(e)
        return {"success":False,"reason":4}
    
async def format_message(data):
    message_uzb = "<b>Foydalanuvchilar:</b>\n"
    message_rus = "<b>Пользователи:</b>\n"
    x = 1

    for j in data:
        sdata = await get_user_profile(j["telegram_user_id"])
        if sdata:
            message_uzb += f"<b>{x}.</b> @{sdata.username}\n"
            message_rus += f"<b>{x}.</b> @{sdata.username}\n"
            x += 1

    return {"uzb": message_uzb, "rus": message_rus}



