from bot_instance import bot

def show_all_channels(channels):
    message_uzb = "Chatlar\n\n"
    message_rus = "Чаты\n\n"
    x = 1
    
    for channel in channels:
        message_uzb += f"""<b>{x}. {channel["username"]}</b> 
<b>Reklama yoqilgan:</b> <i>{channel["for_post_ads"]}</i>
<b>Obuna Shart:</b> <i>{channel["for_users_to_follow"]}</i>
<b>Yangilarni kutib olish:</b> <i>{channel["for_work_as_admin"]}</i>
~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""

        message_rus += f"""<b>{x}. {channel["username"]}</b> 
<b>Реклама включена:</b> <i>{channel["for_post_ads"]}</i>
<b>Обязательная подписка:</b> <i>{channel["for_users_to_follow"]}</i>
<b>Приветствие новых участников:</b> <i>{channel["for_work_as_admin"]}</i>
~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"""
        
        x += 1

    return {"uzb": message_uzb, "rus": message_rus}



def show_all_chats_rmt(channels):
    message_uzb = "Chatlar\n\n"
    message_rus = "Чаты\n\n"
    x = 1
    for channel in channels:
        message_uzb += f"""<b>{x}. {channel["username"]}</b>\n"""
        message_rus += f"""<b>{x}. {channel["username"]}</b>\n"""
        x += 1
    return {"uzb": message_uzb, "rus": message_rus}





async def show_all_admin(admins):
    inactive_ones = []
    xd = {"absolute_admin": {"uzb": "Super admin", "rus": "Супер админ"}, "admin": {"uzb": "Admin", "rus": "Админ"}}
    
    message_uzb = "<b>Adminlar</b>:\n"
    message_rus = "<b>Админы</b>:\n"
    x = 1
    
    for admin in admins:
        try:
            user = await bot.get_chat(admin["telegram_user_id"])
            
            message_uzb += f"""<b>{x}</b>.  <b>Foydalanuvchi:</b> @{user.username} 
     <b>Holati:</b> {xd[admin["status"]]["uzb"]} 
     <b>Qo'shilgan sana:</b> {admin["joined_date"]}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"""
            
            message_rus += f"""<b>{x}</b>.  <b>Имя пользователя:</b> @{user.username} 
     <b>Статус:</b> {xd[admin["status"]]["rus"]} 
     <b>Дата добавления:</b> {admin["joined_date"]}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"""
            
            x += 1
            
        except Exception as e:
            inactive_ones.append(admin)
            
    return {"uzb": message_uzb, "rus": message_rus}



def show_all_bot(bots):
    if bots:
        message = """<b>Botlar</b>:\n"""
        for bot in bots:
            message += f"""
<b>Nomi:</b> {bot[1]}
<b>Username:</b> @{bot[2]}
<b>Tavsifi:</b> {bot[3]}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n
"""
    else:
        message = "Hozircha hech qanday bot mavjud emas..."

    return message
def add_new_admin_2_1t_mt():
    q1 = "<i>Yangi admin holatini tanlang:</i>"
    q2 = "<i>Выберите статус нового администратора:</i>"
    return {"uzb": q1, "rus": q2}

def add_new_admin_2_3t_mt():
    q1 = "<i>Kontakt yoki foydalanuvchi ID raqamini kiriting...</i>"
    q2 = "<i>Введите контакт или ID пользователя...</i>"
    return {"uzb": q1, "rus": q2}


def admin_added_success_mt():
    q1 = "<i>Admin muvaffaqiyatli qo'shildi!</i>"
    q2 = "<i>Админ успешно добавлен!</i>"
    return {"uzb": q1, "rus": q2}


def add_new_admin_1_mt():
    q1 = "<i>Kontakt yuboring yoki foydalanuvchi ID raqamini kiriting:</i>"
    q2 = "<i>Отправьте контакт или введите ID пользователя:</i>"
    return {"uzb": q1, "rus": q2}


def admin_removal_success_mt():
    q1 = "<i>Admin muvaffaqiyatli o'chirildi!</i>"
    q2 = "<i>Администратор успешно удален!</i>"
    return {"uzb": q1, "rus": q2}

def remove_admin_else_m():
    message_uzb = "O'zingizdan boshqa admin mavjud emas!"
    message_rus = "Кроме вас других администраторов нет!"
    return {"uzb": message_uzb, "rus": message_rus}

def add_channel_1_mt():
    q1 = "Kanal yoki guruhning usernameni yuboring:\nMisol: @kanal_username"
    q2 = "Отправьте имя пользователя канала или группы:\nПример: @kanal_username"
    return {"uzb": q1, "rus": q2}

def add_channel_2_mt():
    q1 = "Bot bu chatda e'lon beradimi?"
    q2 = "Бот публикует объявление в этом чате?"
    return {"uzb": q1, "rus": q2}

def add_channel_3_mt():
    q1 = "Botni ishlatish uchun foydalanuvchilar bu chatni kuzatishsinmi?"
    q2 = "Пользователи должны следить за этим чатом для использования бота?"
    return {"uzb": q1, "rus": q2}

def add_channel_4_mt():
    q1 = "Bot bu chatda yangi kuzatuvchilarni kutib olsinmi?"
    q2 = "Бот должен приветствовать новых участников в этом чате?"
    return {"uzb": q1, "rus": q2}

def add_channel_success_mt():
    q1 = "Yangi chat muofaqyatli qo'shildi!"
    q2 = "Новый чат успешно добавлен!"
    return {"uzb": q1, "rus": q2}

def admin_confirmed_1_mt():
    q1="<i>E'lon muofaqyatlik qo'yildi!</i>"
    q2="<i>Объявление одобрено!</i>"
    return {"uzb":q1,"rus":q2}
def admin_confirmed_2_mt():
    q1="<i>E'lon rad etildi!</i>"
    q2="<i>Объявление отклонено!</i>"
    return {"uzb":q1,"rus":q2}

def user_notificated_1_mt():
    q1="<i>E'loningiz muofaqyatlik joylandi!</i>"
    q2="<i>Ваше объявление одобрено!</i>"
    return {"uzb":q1,"rus":q2}

def user_notificated_2_mt():
    q1="<i>E'loningiz admin tomondian tasdiqlanmadi!</i>"
    q2="<i>Ваше объявление не одобрено администратором!</i>"
    return {"uzb":q1,"rus":q2}

def bot_not_worthy_1_mt():
    q1="<i>Bot bu chatda kerakli ruxsatlarga ega emas!</i>"
    q2="<i>У бота нет необходимых разрешений в этом чате!</i>"
    return {"uzb":q1,"rus":q2}   


def bot_was_kicked_mt():
    q1="<i>Bot bu chatdan chiqarib yuborilgan yoki qo'shilmagan!</i>"
    q2="<i>Бот выгнан или не добавлен в этот чат!</i>"  
    return {"uzb":q1,"rus":q2}   

def bot_chat_not_found_mt():
    q1="<i>Chat topilmadi!</i>"
    q2="<i>Чат не найден!</i>" 
    return {"uzb":q1,"rus":q2}   

def sww_mt():
    q1="<i>Nimadir xato ketdi!</i>"
    q2="<i>Что-то пошло не так!</i>"
    return {"uzb":q1,"rus":q2}   
def chat_exists(username):
    umessage_uzb = f"{username} allaqachon bor!"
    umessage_rus = f"{username} уже существует!"
    return {"uzb": umessage_uzb, "rus": umessage_rus}

def ad_showcase_v(data):
    umessage = "<b>Xodim kerak:</b>\n\n"
    umessage += f"🏢<b>Kompaniya:</b> {data['company']}\n"
    umessage += f"📚<b>Texnologiya:</b> {data['skills']}\n"
    umessage += f"📋<b>Faoliyat:</b> {data['activity']}\n"
    if data["username"] is not None:
        umessage += f"📫<b>Telegram:</b> @{data['username']}\n"
    umessage += f"☎️<b>Aloqa:</b> {data['phone_number']}\n"
    umessage += f"🌐<b>Hudud:</b> {data['territory']}\n"
    umessage += f"👤<b>Mas'ul:</b> {data['hr']}\n"
    umessage += f"⏰<b>Murojaat vaqti:</b> {data['request_time']}\n"
    umessage += f"🕒<b>Ish vaqti:</b> {data['work_time']}\n"
    umessage += f"💰<b>Maosh:</b> {data['salary']}\n"
    umessage += f"📋<b>Qo'shimcha:</b> {data['additionals']}\n"
    rmessage = "<b>Нужен сотрудник:</b>\n\n"
    rmessage += f"🏢<b>Компания:</b> {data['company']}\n"
    rmessage += f"📚<b>Технология:</b> {data['skills']}\n"
    rmessage += f"ℹ️<b>Деятельность:</b> {data['activity']}\n"
    if data["username"] is not None:
        rmessage += f"📫<b>Телеграмм:</b> @{data['username']}\n"
    rmessage += f"☎️<b>Контакт:</b> {data['phone_number']}\n"
    rmessage += f"🌐<b>Регион:</b> {data['territory']}\n"
    rmessage += f"👤<b>Ответственный:</b> {data['hr']}\n"
    rmessage += f"⏰<b>Время обращения:</b> {data['request_time']}\n"
    rmessage += f"🕒<b>Рабочее время:</b> {data['work_time']}\n"
    rmessage += f"💰<b>Зарплата:</b> {data['salary']}\n"
    rmessage += f"📋<b>Дополнительно:</b> {data['additionals']}\n"
    return {"uzb":umessage,"rus":rmessage}

def ad_showcase_e(data, ):
    umessage = "<b>Ish joyi kerak:</b>\n\n"
    umessage += f"👨‍💼<b>Xodim:</b> {data['name']}\n"
    umessage += f"📅<b>Yosh:</b> {data['age']}\n"
    umessage += f"💼<b>Kasb:</b> {data['job']}\n"
    umessage += f"📊<b>Tajriba:</b> {data['experience']}\n"
    umessage += f"📚<b>Texnologiya:</b> {data['skills']}\n"
    if data["username"] is not None:
        umessage += f"📫<b>Telegram:</b> @{data['username']}\n"
    umessage += f"☎️<b>Aloqa:</b> {data['phone_number']}\n"
    umessage += f"🌐<b>Hudud:</b> {data['territory']}\n"
    umessage += f"💰<b>Maosh:</b> {data['salary']}\n"
    umessage += f"📋<b>Qo'shimcha:</b> {data['additionals']}\n"
    rmessage = "<b>Требуется место работы:</b>\n\n"
    rmessage += f"👨‍💼<b>Сотрудник:</b> {data['name']}\n"
    rmessage += f"📅<b>Возраст:</b> {data['age']}\n"
    rmessage += f"💼<b>Профессия:</b> {data['job']}\n"
    rmessage += f"📊<b>Опыт:</b> {data['experience']}\n"
    rmessage += f"📚<b>Технологии:</b> {data['skills']}\n"
    if data["username"] is not None:
        rmessage += f"📫<b>Телеграмм:</b> @{data['username']}\n"
    rmessage += f"☎️<b>Контакт:</b> {data['phone_number']}\n"
    rmessage += f"🌐<b>Регион:</b> {data['territory']}\n"
    rmessage += f"💰<b>Зарплата:</b> {data['salary']}\n"
    rmessage += f"📋<b>Дополнительно:</b> {data['additionals']}\n"

    return {"uzb":umessage,"rus":rmessage}

def ad_showcase_p(data,):
    umessage = "<b>Sherik kerak:</b>\n\n"
    umessage += f"👨‍💼<b>Sherik:</b> {data['name']}\n"
    umessage += f"ℹ️<b>Faoliyat:</b> {data['activity']}\n"
    if data["username"] is not None:
        umessage += f"📫<b>Telegram:</b> @{data['username']}\n"
    umessage += f"☎️<b>Aloqa:</b> {data['phone_number']}\n"
    umessage += f"🌐<b>Hudud:</b> {data['territory']}\n"
    umessage += f"📋<b>Qo'shimcha:</b> {data['additionals']}\n"
    rmessage = "<b>Нужен партнер:</b>\n\n"
    rmessage += f"👨‍💼<b>Партнер:</b> {data['name']}\n"
    rmessage += f"ℹ️<b>Деятельность:</b> {data['activity']}\n"
    if data["username"] is not None:
        rmessage += f"📫<b>Телеграмм:</b> @{data['username']}\n"
    rmessage += f"☎️<b>Контакт:</b> {data['phone_number']}\n"
    rmessage += f"🌐<b>Регион:</b> {data['territory']}\n"
    rmessage += f"📋<b>Дополнительно:</b> {data['additionals']}\n"

    return {"uzb":umessage,"rus":rmessage}

