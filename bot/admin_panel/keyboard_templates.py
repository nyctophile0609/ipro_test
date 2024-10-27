from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove


def remove_chat_ikt(channels):
    builder=InlineKeyboardBuilder()
    for i,channel in enumerate(channels):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f"{i+1}",callback_data=f"chat#$removed#${channel["id"]}"))
        else:
            builder.add(types.InlineKeyboardButton(text=f"{i+1}",callback_data=f"chat#$removed#${channel["id"]}"))

    return builder.as_markup() 

def yes_no_rkt():
    # data = {"uzb":["Ha","Yo'q"], "rus": ["Да","Нет"]}[lang]
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Ha"), types.KeyboardButton(text="Yo'q"))
    return builder.as_markup(resize_keyboard=True)

def add_admin_3k():
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Admin absolute",callback_data="newadmin#$absolute"),
        types.InlineKeyboardButton(text="Admin ordinary",callback_data="newadmin#$ordinary"))
    return builder.as_markup()


def show_all_admin_i(data):
    builder=InlineKeyboardBuilder()
    for i,j in enumerate(data):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'admin$#id#${j["telegram_user_id"]}'))
        else:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'admin$#id#${j["telegram_user_id"]}'))
    return builder.as_markup()

def show_all_new_admin_i(data):
    builder=InlineKeyboardBuilder()
    for i,j in enumerate(data):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'new#admin$#id#${j["telegram_user_id"]}'))
        else:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'new#admin$#id#${j["telegram_user_id"]}'))
    return builder.as_markup()

def show_all_new_admin_fr_i(data):
    builder=InlineKeyboardBuilder()
    for i,j in enumerate(data):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'new#$admin$#id#$fr#${j["new_admin_username"]}'))
        else:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}.',callback_data=f'new#$admin$#id#$fr#${j["new_admin_username"]}'))
    return builder.as_markup()
def remove_keyword_i(data:list,checks_it:list):
    builder=InlineKeyboardBuilder()
    x=len(data)
    for i in range (x):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'remove#keyword#num#{data[i]["id"]}'))
        else:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'remove#keyword#num#{data[i]["id"]}'))

    if checks_it==[1,1]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data="remove#keyword#page#back"))
        builder.add(types.InlineKeyboardButton(text=f'Next',callback_data="remove#keyword#page#next"))
    elif checks_it[0]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data="remove#keyword#page#back"))
    elif checks_it[1]:
        builder.row(types.InlineKeyboardButton(text=f'Next',callback_data="remove#keyword#page#next"))

    return builder.as_markup()

def show_keyword_i(checks_it:list):
    builder=InlineKeyboardBuilder()
    if checks_it==[1,1]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data="show#keyword#page#back"))
        builder.add(types.InlineKeyboardButton(text=f'Next',callback_data="show#keyword#page#next"))
    elif checks_it[0]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data="show#keyword#page#back"))
    elif checks_it[1]:
        builder.row(types.InlineKeyboardButton(text=f'Next',callback_data="show#keyword#page#next"))
    return builder.as_markup()


def cr_inline_keyboard(data:list,call_data:list,checks_it:list):
    builder=InlineKeyboardBuilder()

    x=len(data)
    for i in range (x):
        if i%4<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'{call_data[2]}_{data[i][0]}'))
        elif i%4<2:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'{call_data[2]}_{data[i][0]}'))
        elif i%4<3:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'{call_data[2]}_{data[i][0]}'))
        elif i%4:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'{call_data[2]}_{data[i][0]}'))
        
    if checks_it==[1,0]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data=call_data[0]))
    elif checks_it==[0,1]:
        builder.row(types.InlineKeyboardButton(text=f'Next',callback_data=call_data[1]))
    elif checks_it==[1,1]:
        builder.row(types.InlineKeyboardButton(text=f'Back',callback_data=call_data[0]),
        types.InlineKeyboardButton(text='Next',callback_data=call_data[1]))
    if len(call_data)==4:
        builder.row(types.InlineKeyboardButton(text=f'Done',callback_data=call_data[3]))