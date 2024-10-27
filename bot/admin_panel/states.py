from aiogram.fsm.state import State, StatesGroup

from aiogram.fsm.state import State, StatesGroup


class AdminCreation(StatesGroup):
    telegram_id=State()
    admin_status=State()


class AddChannel(StatesGroup):
    channel_username=State()
    for_work_as_admin=State()
    for_post_ads=State()
    for_users_to_follow=State()
    
    
