from aiogram.filters import Command, StateFilter
from aiogram import Router,types,F
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State  # Correct import for State
from aiogram.types import ContentType  # 
import shutil
import os
import datetime
import time
from database.db import *
from .message_templates import *
from .additionals import *
from .keyboards import *
from .states import *
customer_panel_router=Router()
user_data=dict()

@customer_panel_router.message(Command("start"))
async def start_func(msg:types.Message,state:FSMContext):
    channels_sp1=get_channels_sp1()
    channels_sp2=get_channels_sp2()
    if is_admin(msg.from_user.id):
        update_admin_chat_id(msg.from_user.id,msg.chat.id)
        await msg.reply("you r admin",)
    
    elif is_user(msg.from_user.id) and await is_chat_member_loop(channels_sp1,msg.from_user.id):
        user=get_user(msg.from_user.id)
        if channels_sp2:
            text,clue=choose_channel_mt(channels_sp2,user["lang"])
            await msg.answer(text, reply_markup=choose_channel_rkt(channels_sp2))
            await state.set_state(General.channel)
            await state.set_data({"channel_id_clue":clue})

        else:
            await msg.answer("No channels")

    elif await is_chat_member_loop(channels_sp1,msg.from_user.id) :
        await msg.reply(choose_language_ur_mt,reply_markup=choose_language_kt())

    elif not await is_chat_member_loop(channels_sp1,msg.from_user.id) :
        await msg.reply(follow_the_channels_ur_mt,reply_markup=follow_the_channels_kt(channels_sp1))
    


@customer_panel_router.callback_query(F.data.startswith("following#$channels_sp1#$done"))
async def channels_followed(callback: types.callback_query,state:FSMContext):
    channels_sp1=get_channels_sp1()
    channels_sp2=get_channels_sp2()

    if is_chat_member_loop(channels_sp1,callback.from_user.id):
        if is_user(callback.from_user.id) and channels_sp2:
            user=get_user(callback.from_user.id)
            text,clue=choose_channel_mt(channels_sp2,user["lang"])
            await callback.message.answer(text, reply_markup=choose_channel_rkt(channels_sp2))
            await state.set_state(General.channel)
            await state.set_data({"channel_id_clue":clue})

        elif not is_user(callback.from_user.id):
            await callback.message.answer(choose_language_ur_mt,reply_markup=choose_language_kt())
        else:
            await callback.message.answer("No channels yet")
    else:
        await callback.message.answer(follow_the_channels_ur_mt,reply_markup=follow_the_channels_kt(channels_sp1))
    callback.answer()


@customer_panel_router.message(Command("change_lang"))
async def change_lang(msg:types.Message):
    await msg.reply(choose_language_ur_mt,reply_markup=choose_language_kt())



@customer_panel_router.callback_query(F.data.startswith("prefered#$language#$"))
async def language_updated(callback: types.callback_query,state:FSMContext):
    lang="uzb" if "uzb" in callback.data else "rus"
    channels_sp2=get_channels_sp2()
    if is_admin(callback.from_user.id):
        update_admin_lang(callback.from_user.id)
        await callback.message.edit_text(language_updated_mt(lang))
    elif is_user(callback.from_user.id):
        update_user_lang(callback.from_user.id,lang)
        await callback.message.edit_text(language_updated_mt(lang))
        text,clue=choose_channel_mt(channels_sp2,user["lang"])
        await callback.message.answer( text,reply_markup=choose_channel_rkt(channels_sp2))
        await state.set_state(General.channel)
        await state.set_data({"channel_id_clue":clue})

        

    else:
        if create_user(callback.from_user.id,lang):
            user=get_user(callback.from_user.id)
            text,clue=choose_channel_mt(channels_sp2,user["lang"])
            await callback.message.answer(text, reply_markup=choose_channel_rkt(channels_sp2))
            await state.set_state(General.channel)
            await state.set_data({"channel_id_clue":clue})

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
@customer_panel_router.message(StateFilter(General.channel))
async def channel_choosen(msg:types.Message,state:FSMContext):
    data=await state.get_data()
    if msg.text in data["channel_id_clue"].keys():
        data["channel_id"]=data["channel_id_clue"][msg.text]
        data["username"]=msg.from_user.username
        data["telegram_id"]=msg.from_user.id
        data["channel"]=get_channel(data["channel_id"])["username"]
        user=get_user(msg.from_user.id)
        await state.set_data(data)
        await state.set_state(General.ad_type)
        await msg.answer(info_post_add_mt(user["lang"]),reply_markup=choose_ad_type_rkt(user["lang"]))    

@customer_panel_router.message(StateFilter(General.ad_type))
async def ad_type_choosen(msg:types.Message,state:FSMContext):
    if is_user(msg.from_user.id):
        
        data=await state.get_data()
        user=get_user(msg.from_user.id)
        mesg=msg.text
        if mesg in ad_type_callback_d_ur_sp[0]:
            data["ad_type"]=0
            await state.set_state(AdVacancy.company)
            await msg.reply(company_message(user["lang"]),reply_markup=ReplyKeyboardRemove())
        elif mesg in ad_type_callback_d_ur_sp[1]:
            data["ad_type"]=1
            await msg.reply(name_message(user["lang"]),reply_markup=ReplyKeyboardRemove())
            await state.set_state(AdEmployee.name)
        elif mesg in ad_type_callback_d_ur_sp[2]:
            data["ad_type"]=2
            await msg.reply(name_message(user["lang"]),reply_markup=ReplyKeyboardRemove())
            await state.set_state(AdPartner.name)
        await state.set_data(data)




async def ultimate_handler_v(msg: types.Message, state: FSMContext, state_name: str, next_state: State, message: str):
    if is_user(msg.from_user.id):
        user=get_user(msg.from_user.id)
        lang=user["lang"]
        mesg = msg.text
        current_data = await state.get_data()  # Get the current state data
        current_data[state_name] = mesg 
        # print(current_data) # Update the specific field
        await state.set_data(current_data)  # Set the updated data back to state
        await state.set_state(next_state)  
        await msg.reply(message,reply_markup=back_to_the_past_ikt(lang))
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
@customer_panel_router.message(StateFilter(AdVacancy.company))
async def handle_skills(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "company", AdVacancy.skills,skills_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.skills))
async def handle_company(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "skills", AdVacancy.activity, activity_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.activity))
async def handle_activity(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "activity", AdVacancy.hr, hr_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.hr))
async def handle_hr(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "hr", AdVacancy.phone_number, phone_number_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.phone_number))
async def handle_phone_number(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "phone_number", AdVacancy.territory, territory_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.territory))
async def handle_territory(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "territory", AdVacancy.request_time, request_time_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.request_time))
async def handle_request_time(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "request_time", AdVacancy.work_time, work_time_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.work_time))
async def handle_work_time(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "work_time", AdVacancy.salary, salary_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.salary))
async def handle_salary(msg: types.Message, state: FSMContext):
    user=get_user(msg.from_user.id)
    lang=user["lang"]
    await ultimate_handler_v(msg, state, "salary", AdVacancy.additionals, additionals_message(lang))

@customer_panel_router.message(StateFilter(AdVacancy.additionals))
async def handle_additionals(msg: types.Message, state: FSMContext):
    if is_user(msg.from_user.id):
        user=get_user(msg.from_user.id)
        lang=user["lang"]
        data = await state.get_data() 
        data["additionals"] = msg.text 
        await state.set_data(data)  
        await state.set_state(AdVacancy.confirmation)
        channel=get_channel(data["channel_id"])
        data["username"]=msg.from_user.username
        showcase_message=ad_showcase_v(data)
        await msg.answer(showcase_message[lang])
        await msg.reply(text=confirm_message(lang,channel), reply_markup=confirmation_yn_rkt(lang))

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
@customer_panel_router.message(StateFilter(AdEmployee.name))
async def handle_age_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "name", AdEmployee.age, age_message(lang))


@customer_panel_router.message(StateFilter(AdEmployee.age))
async def handle_age_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "age", AdEmployee.job, job_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.job))
async def handle_job_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "job", AdEmployee.experience, experience_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.experience))
async def handle_experience_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "experience", AdEmployee.skills, skills_message_ep(lang))

@customer_panel_router.message(StateFilter(AdEmployee.skills))
async def handle_experience_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "skills", AdEmployee.phone_number, phone_number_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.phone_number))
async def handle_number_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "phone_number", AdEmployee.territory, territory_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.territory))
async def handle_territory_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "territory", AdEmployee.salary, salary_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.salary))
async def handle_salary_e(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "salary", AdEmployee.additionals, additionals_message(lang))

@customer_panel_router.message(StateFilter(AdEmployee.additionals))
async def handle_additionals_e(msg: types.Message, state: FSMContext):
    if is_user(msg.from_user.id):
        user = get_user(msg.from_user.id)
        lang = user["lang"]
        await state.set_state(AdEmployee.confirmation)
        data = await state.get_data() 
        data["additionals"]= msg.text
        await state.set_data(data)

        channel=get_channel(data["channel_id"])
        data["username"]=msg.from_user.username
        showcase_message=ad_showcase_e(data)
        await msg.answer(showcase_message[lang])
        await msg.reply(text=confirm_message(lang,channel), reply_markup=confirmation_yn_rkt(lang))

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
@customer_panel_router.message(StateFilter(AdPartner.name))
async def handle_job_p(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "name", AdPartner.activity, activity_message_ep(lang))

@customer_panel_router.message(StateFilter(AdPartner.activity))
async def handle_job_p(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "activity", AdPartner.phone_number, phone_number_message(lang))

@customer_panel_router.message(StateFilter(AdPartner.phone_number))
async def handle_number_p(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "phone_number", AdPartner.territory, territory_message(lang))

@customer_panel_router.message(StateFilter(AdPartner.territory))
async def handle_territory_p(msg: types.Message, state: FSMContext):
    user = get_user(msg.from_user.id)
    lang = user["lang"]
    await ultimate_handler_v(msg, state, "territory", AdPartner.additionals, additionals_message(lang))

@customer_panel_router.message(StateFilter(AdPartner.additionals))
async def handle_additionals_p(msg: types.Message, state: FSMContext):
    if is_user(msg.from_user.id):
        user = get_user(msg.from_user.id)
        lang = user["lang"]
        await state.set_state(AdPartner.confirmation)
        data = await state.get_data() 
        data["additionals"]=msg.text
        await state.set_data(data)

        print(data)
        channel=get_channel(data["channel_id"])
        data["username"]=msg.from_user.username
        showcase_message=ad_showcase_p(data)
        await msg.answer(showcase_message[lang])
        await msg.reply(text=confirm_message(lang,channel), reply_markup=confirmation_yn_rkt(lang))



####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
async def handle_confirmation_core(msg: types.Message, state: FSMContext, message: str):
    if is_user(msg.from_user.id):
        lang = get_user(msg.from_user.id)["lang"]
        current_state=await state.get_state()
        if msg.text in (confirmation_data_ur[0], confirmation_data_ur[2]) and current_state:
            data = await state.get_data() 
            if msg.text in confirmation_data_ur:
                if current_state.startswith("AdVacancy"):
                    print(1)
                    id=create_ads_vacancy(data)
                    ad_type="vacancy"
                    noficlation1=ad_showcase_v(data)
                elif current_state.startswith("AdEmployee"):
                    print(2)
                    ad_type="employee"
                    id=create_ads_employee(data)
                    noficlation1=ad_showcase_e(data)
                elif current_state.startswith("AdPartner") and create_ads_partner(data):
                    print(3)
                    ad_type="partner"
                    id=create_ads_partner(data)
                    noficlation1=ad_showcase_p(data)
                admins=get_admins()
                if admins!=[]:
                    for admin in admins:
                        noficlation2=admin_confirmation_mt(data,lang)
                        try:
                            await bot.send_message(admin["telegram_user_id"],text=noficlation1[admin["lang"]],)
                            await bot.send_message(admin["telegram_user_id"],text=noficlation2,reply_markup=yes_no_admin_ikt(admin["lang"],id,ad_type))

                        except Exception:
                            pass
                    await msg.reply(done_message(lang))
                    await state.clear()



            elif msg.text in (confirmation_data_ur[1], confirmation_data_ur[3]):
                await msg.reply(confirm_message_false(user["lang"]))


@customer_panel_router.message(StateFilter(AdVacancy.confirmation))
async def handle_confirmation_e(msg:types.Message,state:FSMContext):
    await handle_confirmation_core(msg,state,"uifgiusufgsdgfgiusgdfusd",)

@customer_panel_router.message(StateFilter(AdEmployee.confirmation))
async def handle_confirmation_e(msg:types.Message,state:FSMContext):
    await handle_confirmation_core(msg,state,"kjakjncxncksc")

@customer_panel_router.message(StateFilter(AdPartner.confirmation))
async def handle_confirmation_e(msg:types.Message,state:FSMContext):
    await handle_confirmation_core(msg,state,"qwertyuioytrew")

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
@customer_panel_router.callback_query(F.data.startswith("back#$to#$the#$past"))
async def back_to_the_past(callback:types.callback_query,state:FSMContext):
    current_state=await state.get_state()

    if is_user(callback.from_user.id) and current_state:
        lang=get_user(callback.from_user.id)["lang"]
        print(current_state)
        if current_state.startswith("AdVacancy"):
            next_state=advacancy_sp[current_state]
            await state.set_state(next_state)
            await callback.message.edit_text(advacancy_states_mtf(lang,next_state),reply_markup=back_to_the_past_ikt(lang) )

        elif current_state.startswith("AdEmployee"):
            next_state=ademployee_sp[current_state]
            await state.set_state(next_state)
            await callback.message.edit_text(ademployee_states_mtf(lang,next_state) )

        elif current_state.startswith("AdPartner"):
            next_state=adpartner_sp[current_state]
            await state.set_state(next_state)
            await callback.message.edit_text(adpartner_states_mtf(lang,next_state) )
        callback.answer()






