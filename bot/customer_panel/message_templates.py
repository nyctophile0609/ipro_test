choose_language_ur_mt="Choose a language to continue...\nВыберите язык, чтобы продолжить"
follow_the_channels_ur_mt="Follow these  channels to continue...\nПодпишитесь на эти каналы, чтобы продолжить..."


def language_updated_mt(lang):
    return {"uzb":"Til o'zgartirildi!","rus":"Язык обновлен!"}[lang]
    
def info_post_add_mt(lang):
    q={"uzb":"Nima qidiryapsiz?","rus":"Что Вы ищете?"}
    return q[lang]



def choose_channel_mt(channels,lang):
    if channels==None:
        return None
    if lang=="uzb":
        message="<b>Qaysi kanalda e'lon bermoqchisiz?</b>\n\n"
    else:
        message="На каком канале вы хотите опубликовать?\n\n"
    clue=dict()
    for i,channel in enumerate(channels):
        message+=f"{i+1}. {channel["username"]}"
        clue[str(i+1)]=channel["id"]

    return [message,clue]



def skills_message(lang):
    messages = {
        "uzb": "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating.\n Masalan: Java, C++, C#",
        "rus": "📚 Технология:\n\nВведите необходимые технологии?\nРазделяйте названия технологий запятыми.\n Например: Java, C++, C#."
    }
    return messages[lang]

def skills_message_ep(lang):
    messages = {
        "uzb": "📚 Texnologiya:\n\nBiladigan texnologiyalaringizni kiriting:\nTexnologiya nomlarini vergul bilan ajrating.\n Masalan: Java, C++, C#",
        "rus": "📚 Технология:\n\nУкажите технологии, которые вы знаете:\nРазделяйте названия технологий запятыми.\n Например: Java, C++, C#."
    }
    return messages[lang]

def company_message(lang):
    messages = {
        "uzb": "🏢 Kompaniya nomini kiriting:\n\nKompaniyangizning to'liq nomini kiriting.",
        "rus": "🏢 Введите название компании:\n\nВведите полное название вашей компании."
    }
    return messages[lang]

def activity_message(lang):
    messages = {
        "uzb": "📋 Faoliyatingizni kiriting:\n\nKompaniyangizning faoliyat yo'nalishini yozing.",
        "rus": "📋 Введите вашу деятельность:\n\nВведите направление деятельности вашей компании."
    }
    return messages[lang]

def activity_message_ep(lang):
    messages = {
        "uzb": "📋 Faoliyatingizni kiriting:",
        "rus": "📋 Введите вашу деятельность:"
    }
    return messages[lang]


def hr_message(lang):
    messages = {
        "uzb": "👤 Mas'ul shaxsning ismini kiriting",
        "rus": "👤 Введите имя ответственного лица"
    }
    return messages[lang]

def phone_number_message(lang):
    messages = {
        "uzb": "☎️ Aloqa:\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67",
        "rus": "☎️ Контакт:\n\nВведите свой контактный номер?\nНапример, +998 90 123 45 67",
    }
    return messages[lang]

def territory_message(lang):
    messages = {
        "uzb": "🌐 Hudud\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.",
        "rus": "🌐 Регион\n\nИз какого вы региона?\nВведите название региона, города Ташкента или Республики.",
    }
    return messages[lang]

def request_time_message(lang):
    messages = {
        "uzb": "⏰ Murojaat qilish vaqti:\n\n Qaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00",
        "rus": "⏰ Время подачи заявки:\n\n Когда можно подать заявку?\nНапример, с 9:00 до 18:00"
    }
    return messages[lang]

def work_time_message(lang):
    messages = {
        "uzb": "🕒 Ish vaqtini kiriting:",
        "rus": "🕒 Введите рабочее время:"
    }
    return messages[lang]

def salary_message(lang):
    messages = {
        "uzb": "💰 Maoshni kiriting:",
        "rus": "💰 Введите зарплату:"
    }
    return messages[lang]

def additionals_message(lang):
    messages = {
        "uzb": "📋 Qo'shimcha ma'lumotlar:",
        "rus": "📋 Дополнительная информация:"
    }
    return messages[lang]

def name_message(lang):
    messages = {
        "uzb": "👤 Ism, familyangizni kiriting:",
        "rus": "👤 Введите свое имя и фамилию:"
    }
    return messages[lang]

def age_message(lang):
    messages = {
        "uzb": "📅 Yoshingizni kiriting:",
        "rus": "📅 Введите ваш возраст:"
    }
    return messages[lang]

def job_message(lang):
    messages = {
        "uzb": "💼 Kasbingizni kiriting:\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan: Talaba",
        "rus": "💼 Введите род занятий:\n\nВы работаете или учитесь?\nПример: Студент"
    }
    return messages[lang]

def experience_message(lang):
    messages = {
        "uzb": "📊 Tajribangizni kiriting:",
        "rus": "📊 Введите ваш опыт:"
    }
    return messages[lang]


def confirm_message(lang,channel):
    messages = {
        "uzb": f"E'loningiz {channel["username"]} da qo'yiladi!\nBarcha ma'lumotlar to'g'rimi? ",
        "rus": f"Ваше объявление будет размещено в {channel['username']}!\nВся информация верна?"
    }
    return messages[lang]   

def done_message(lang):
    messages = {
        "uzb": f"E'loningiz adminga jo'natildi! ",
        "rus": f"Ваше объявление отправлено администратору!"
    }
    return messages[lang]   

def confirm_message_false(lang):
    messages = {
        "uzb": "Qabul qilinmadi!",
        "rus": "Не принято!"
    }
    return messages[lang]   

def admin_confirmation_mt(data,lang):
    messages={"uzb":f"<b>Yangi e'lon!</b>\n@{data["username"]} {data["channel"]} da yuqoridagi e'lonni qo'ymoqchi...\n<i>E'lonni tasdiqlaysizmi?</i>",
        "rus":f"<b>Новое объявление!</b>\n@{data['username']} хочет разместить объявление на {data['channel']}...\n<i>Вы подтверждаете объявление?</i>"}
    return messages[lang]


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

