from aiogram.filters import Command,StateFilter
from aiogram import Router,types,F
from aiogram.fsm.context import FSMContext
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ReplyKeyboardRemove

from database.db import *
from .message_templates import *
from .keyboard_templates import *
from .states import *
from .additionals import *
admin_panel_router=Router()
user_data={}




@admin_panel_router.message(Command("admins"))
async def show_all_admins(msg:types.Message):
    if is_absolute_admin(msg.from_user.id):
        admin=get_admin(msg.from_user.id)
        admins=await show_all_admin(get_admins())
        admins=admins[admin["lang"]]
        await msg.reply(admins)

# ############################################################################################
# ############################################################################################
# ############################################################################################
@admin_panel_router.message(Command("remove_admin"))
async def remove_admin_1(msg:types.Message):
    if is_absolute_admin(msg.from_user.id):
        all_users=get_only_admins()
        admin=get_admin(msg.from_user.id)
        if all_users!=[]:
            text=(await format_message(all_users))[admin["lang"]]
            await msg.reply(text,reply_markup=show_all_admin_i(all_users))
        else:
            await msg.reply(remove_admin_else_m()[admin["lang"]])

@admin_panel_router.callback_query(F.data.startswith("admin$#id#$"))
async def remove_admin_2(callback: types.callback_query):
    if is_absolute_admin(callback.from_user.id):
        admin_id = callback.data.split("admin$#id#$")[1]
        admin=get_admin(callback.from_user.id)
        if delete_admin(admin_id):
            await callback.message.edit_text(admin_removal_success_mt()[admin["lang"]])
        else:
            await callback.message.edit_text(sww_mt()[admin["lang"]])


############################################################################################
############################################################################################
###########################################################################################

@admin_panel_router.message(Command("add_admin"))
async def add_admin_1(msg:types.Message,state:FSMContext):
    if is_absolute_admin(msg.from_user.id):     
        admin=get_admin(msg.from_user.id)           
        await msg.reply(add_new_admin_1_mt()[admin["lang"]])
        await state.set_state(AdminCreation.telegram_id)
 

@admin_panel_router.message(AdminCreation.telegram_id)
async def add_admin_2(msg:types.Message,state:FSMContext):
    if is_absolute_admin(msg.from_user.id):  
        admin=get_admin(msg.from_user.id )    
        print(msg.text)
        if msg.contact:     
            await state.set_data({"telegram_id": msg.contact.user_id})   
            print(msg.contact.user_id)
            await msg.reply(add_new_admin_2_1t_mt()[admin["lang"]],reply_markup=add_admin_3k())
            print(await get_user_profile(msg.contact.user_id))
        elif msg.text.isnumeric() and await get_user_profile(msg.text)!=False:     
            await state.set_data({"telegram_id": msg.text})   
            print(msg.text)
            print(await get_user_profile(msg.text))
            await msg.reply(add_new_admin_2_1t_mt()[admin["lang"]],reply_markup=add_admin_3k())
        else:
            await msg.reply(add_new_admin_2_3t_mt()[admin["lang"]])

@admin_panel_router.callback_query(F.data.startswith("newadmin#$"))
async def add_admin_3(callback:types.callback_query,state:FSMContext):
    with suppress(TelegramBadRequest):
        if is_absolute_admin(callback.from_user.id): 
            admin=get_admin(callback.from_user.id)      
            status="absolute_admin" if "absolute" in callback.data else "admin"
            data = await state.get_data()
            na_id = data.get("telegram_id") 
            pna_id=await get_user_profile(na_id)
            if pna_id!=False and is_admin(pna_id.id) and update_admin_status(pna_id,status):
                await callback.message.edit_text(admin_added_success_mt()[admin['lang']])
                await state.clear()                      
            if create_admin(na_id,status):
                await callback.message.edit_text(admin_added_success_mt()[admin['lang']])
                await state.clear()
            else:
                await callback.message.edit_text(sww_mt()[admin["lang"]])




############################################################################################
############################################################################################
############################################################################################
@admin_panel_router.message(Command("channels"))
async def show_all_admins(msg:types.Message):
    if is_admin(msg.from_user.id):
        admin=get_admin(msg.from_user.id)
        channels=show_all_channels(get_channels())[admin["lang"]]
        await msg.reply(channels)










############################################################################################
############################################################################################
############################################################################################
@admin_panel_router.message(Command("add_channel"))
async def add_channel_1(msg:types.Message,state:FSMContext):
    if is_admin(msg.from_user.id):
        admin=get_admin(msg.from_user.id)
        await msg.reply(add_channel_1_mt()[admin["lang"]])
        await state.set_state(AddChannel.channel_username)

@admin_panel_router.message(StateFilter(AddChannel.channel_username))
async def add_channel_1(msg:types.Message,state:FSMContext):
    if is_admin(msg.from_user.id):
        admin=get_admin(msg.from_user.id)
        username=format_the_username(msg.text)
        if is_channel_exists(username):
            res=await is_bot_worthy(username)
            print(res)
            if res["success"]:
                await state.set_data({"username":username})
                await state.set_state(AddChannel.for_post_ads)
                await msg.reply(add_channel_2_mt()[admin["lang"]],reply_markup=yes_no_rkt())
            elif res["reason"]==1:
                await msg.reply(bot_not_worthy_1_mt()[admin["lang"]])
            elif res["reason"]==2:
                await msg.reply(bot_was_kicked_mt()[admin["lang"]])
            elif res["reason"]==3:
                await msg.reply(bot_chat_not_found_mt()[admin["lang"]])
            elif res["reason"]==4:
                await msg.reply(sww_mt()[admin["lang"]])
        else:
            await msg.reply(text=chat_exists(username)[admin["lang"]])

@admin_panel_router.message(StateFilter(AddChannel.for_post_ads))
async def add_channel_1(msg:types.Message,state:FSMContext):
    if is_admin(msg.from_user.id) and msg.text.lower() in ["ha","yo'q"]:
        admin=get_admin(msg.from_user.id)
        data=await state.get_data()
        data["for_post_ads"]={"ha":True,"yo'q":False}[msg.text.lower()]
        await state.set_data(data)
        await state.set_state(AddChannel.for_users_to_follow)
        await msg.reply(add_channel_3_mt()[admin["lang"]],reply_markup=yes_no_rkt())

@admin_panel_router.message(StateFilter(AddChannel.for_users_to_follow))
async def add_channel_1(msg:types.Message,state:FSMContext):
    if is_admin(msg.from_user.id) and msg.text.lower() in ["ha","yo'q"]:
        admin=get_admin(msg.from_user.id)
        data=await state.get_data()
        data["for_users_to_follow"]={"ha":True,"yo'q":False}[msg.text.lower()]
        await state.set_data(data)
        await state.set_state(AddChannel.for_work_as_admin)
        await msg.reply(add_channel_4_mt()[admin["lang"]],reply_markup=yes_no_rkt())

@admin_panel_router.message(StateFilter(AddChannel.for_work_as_admin))
async def add_channel_1(msg:types.Message,state:FSMContext):
    if is_admin(msg.from_user.id) and msg.text.lower() in ["ha","yo'q"]:
        admin=get_admin(msg.from_user.id)
        data=await state.get_data()
        data["for_work_as_admin"]={"ha":True,"yo'q":False}[msg.text.lower()]
        await state.clear()
        if create_channel(data):
            await msg.reply(add_channel_success_mt()[admin["lang"]])
        else:
            await msg.reply(sww_mt()[admin["lang"]])

############################################################################################
############################################################################################
###########################################################################################

@admin_panel_router.message(Command("remove_chat"))
async def remove_channel_1(msg:types.Message):
    if is_absolute_admin(msg.from_user.id):
        admin=get_admin(msg.from_user.id)
        channels=get_channels()
        text=show_all_chats_rmt(channels)[admin["lang"]]
        await msg.reply(text=text,reply_markup=remove_chat_ikt(channels))


@admin_panel_router.callback_query(F.data.startswith("chat#$removed#$"))
async def remove_chat_2(callback:types.callback_query):
    if is_admin(callback.from_user.id):
        admin=get_admin(callback.from_user.id)
        chat_id=callback.data.split("chat#$removed#$")[1]
        if delete_channel(chat_id):
            admin=get_admin(callback.from_user.id)
            channels=get_channels()
            text=show_all_chats_rmt(channels)[admin["lang"]]
            await callback.message.edit_text(text=text,reply_markup=remove_chat_ikt(channels))




############################################################################################
############################################################################################
###########################################################################################








############################################################################################
############################################################################################
###########################################################################################
@admin_panel_router.callback_query(F.data.startswith("admin#$confirm#$"))
async def admin_ad_confirmation(callback:types.callback_query):
    if is_admin(callback.from_user.id):
        confirmation=callback.data.split("admin#$confirm#$")[1]
        id,ad_type,yn=confirmation.split("%")
        admin=get_admin(callback.from_user.id)
        ad={"vacancy":get_ads_vacancy,"employee":get_ads_employee,"partner":get_ads_partner}[ad_type](id)
        user=get_user(ad["telegram_id"])

        if yn=="yes":
            user_profile=await get_user_profile(ad["telegram_id"])
            ad["username"]=user_profile.username
            text={"vacancy":ad_showcase_v,"employee":ad_showcase_e,"partner":ad_showcase_p}[ad_type](ad)[admin["lang"]]
            await bot.send_message(ad["channel"],text)
            await callback.message.edit_text(admin_confirmed_1_mt()[admin["lang"]])
            await bot.send_message(ad["telegram_id"],user_notificated_1_mt()[user["lang"]])
        elif yn=="no":
            await callback.message.edit_text(admin_confirmed_2_mt()[admin["lang"]])
            await bot.send_message(ad["telegram_id"],user_notificated_2_mt()[user["lang"]])

    await callback.answer()


