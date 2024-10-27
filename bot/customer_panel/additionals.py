from bot_instance import bot
from .states import *
from .message_templates import *

ad_type_callback_d_ur=("Xodim kerak", "Ish joyi kerak", "Sherik kerak","Нужен сотрудник", "Нужна работа", "Нужен партнер")
ad_type_callback_d_ur_sp=(("Xodim kerak","Нужен сотрудник",),( "Ish joyi kerak","Нужна работа",),( "Sherik kerak","Нужен партнер",),)
confirmation_data_ur=("Ha","Yo'q","Да","Нет")
async def is_chat_member_loop(channels,user_id):
	if channels==[] or channels==None:
		return True
	print(channels)
	
	for channel in channels:
		if not await is_chat_member(channel["username"],user_id):
			return False
	return True

async def is_chat_member(channel_username,user_id):
	member = await bot.get_chat_member(channel_username, user_id)
	if member.status in ['member', 'administrator', 'creator']:
		return True
	return False
  




advacancy_sp = {
    AdVacancy.additionals.state: AdVacancy.salary.state,
    AdVacancy.salary.state: AdVacancy.work_time.state,
    AdVacancy.work_time.state: AdVacancy.request_time.state,
    AdVacancy.request_time.state: AdVacancy.territory.state,
    AdVacancy.territory.state: AdVacancy.phone_number.state,
    AdVacancy.phone_number.state: AdVacancy.hr.state,
    AdVacancy.hr.state: AdVacancy.activity.state,
    AdVacancy.activity.state: AdVacancy.skills.state,
    AdVacancy.skills.state: AdVacancy.company.state
}

ademployee_sp = {
    AdEmployee.additionals.state: AdEmployee.salary.state,
    AdEmployee.salary.state: AdEmployee.territory.state,
    AdEmployee.territory.state: AdEmployee.phone_number.state,
    AdEmployee.phone_number.state: AdEmployee.skills.state,
    AdEmployee.skills.state: AdEmployee.experience.state,
    AdEmployee.experience.state: AdEmployee.job.state,
    AdEmployee.job.state: AdEmployee.age.state,
    AdEmployee.age.state: AdEmployee.name.state
}

adpartner_sp = {
    AdPartner.additionals.state: AdPartner.territory.state,
    AdPartner.territory.state: AdPartner.phone_number.state,
    AdPartner.phone_number.state: AdPartner.activity.state,
    AdPartner.activity.state: AdPartner.name.state
}
def advacancy_states_mtf(lang,state):

	advacancy_states_mt = {
		AdVacancy.company.state: company_message(lang),
		AdVacancy.skills.state: skills_message(lang),
		AdVacancy.activity.state: activity_message(lang),
		AdVacancy.hr.state: hr_message(lang),
		AdVacancy.phone_number.state: phone_number_message(lang),
		AdVacancy.territory.state: territory_message(lang),
		AdVacancy.request_time.state: request_time_message(lang),
		AdVacancy.work_time.state:work_time_message(lang),
		AdVacancy.salary.state: salary_message(lang),
		AdVacancy.additionals.state: additionals_message(lang)
	}
	return advacancy_states_mt[state]

def ademployee_states_mtf(lang,state):


	ademployee_states_mt = {
		AdEmployee.name.state: name_message(lang),
		AdEmployee.age.state: age_message(lang),
		AdEmployee.job.state:job_message(lang),
		AdEmployee.experience.state: experience_message(lang),
		AdEmployee.skills.state: skills_message_ep(lang),
		AdEmployee.phone_number.state: phone_number_message(lang),
		AdEmployee.territory.state: territory_message(lang),
		AdEmployee.salary.state: salary_message(lang),
		AdEmployee.additionals.state:additionals_message(lang)
	}
	return ademployee_states_mt[state]

def adpartner_states_mtf(lang,state):

	adpartner_states_mt = {
		AdPartner.name.state:name_message(lang),
		AdPartner.activity.state: activity_message(lang),
		AdPartner.phone_number.state: phone_number_message(lang),
		AdPartner.territory.state: territory_message(lang),
		AdPartner.additionals.state: additionals_message(lang)
	}

	return adpartner_states_mt[state]

