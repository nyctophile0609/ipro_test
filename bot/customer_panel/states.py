from aiogram.fsm.state import State, StatesGroup

class AdVacancy(StatesGroup):
    company = State()
    skills = State()
    activity = State()
    hr = State()
    phone_number = State()
    territory = State()
    request_time = State()
    work_time = State()
    salary = State()
    additionals = State()
    confirmation=State()

class AdEmployee(StatesGroup):
    name = State()
    age = State()
    job = State()
    experience = State()
    skills = State()
    phone_number = State()
    territory = State()
    salary = State()
    additionals = State()
    confirmation=State()

class AdPartner(StatesGroup):
    name = State()
    activity=State()
    phone_number = State()
    territory = State()
    additionals = State()
    confirmation=State()

class General(StatesGroup):
    channel = State()
    ad_type=State()    


