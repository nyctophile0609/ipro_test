from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
from .additionals import ad_type_callback_d_ur


def follow_the_channels_kt(channels):
    builder=InlineKeyboardBuilder()
    for i, channel in enumerate(channels):
        builder.row(types.InlineKeyboardButton(text=f"{i+1}. Kuzatish/Подписаться",url=f"{channel["username"]}"))
    builder.row(types.InlineKeyboardButton(text=f"Tekshirish/Проверять",callback_data="following#$channels#$done"))
    return builder.as_markup()


def choose_ad_type_rkt(lang):
    data = {"uzb": ad_type_callback_d_ur[:3], "rus": ad_type_callback_d_ur[3:]}[lang]
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text=data[0]), types.KeyboardButton(text=data[1]), types.KeyboardButton(text=data[2]))
    return builder.as_markup(resize_keyboard=True)

def confirmation_yn_rkt(lang):
    data = {"uzb":["Ha","Yo'q"], "rus": ["Да","Нет"]}[lang]
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text=data[0]), types.KeyboardButton(text=data[1]))
    return builder.as_markup(resize_keyboard=True)

def choose_language_kt():
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="O'zbekcha",callback_data="prefered#$language#$uzb"),
        types.InlineKeyboardButton(text="Pусский",callback_data="prefered#$language#$rus"))

    return builder.as_markup()

def choose_ad_type_kt():
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text=f'1.',callback_data=f'prefered#$adtype#$1'))
    builder.add(types.InlineKeyboardButton(text=f'2.',callback_data=f'prefered#$adtype#$2'))
    builder.add(types.InlineKeyboardButton(text=f'3.',callback_data=f'prefered#$adtype#$3'))
    return builder.as_markup()    

def choose_channel_kt(channels):
    if channels==None:
        return None
    builder=InlineKeyboardBuilder()
    for i,j in enumerate(channels):
        if i%5<1:
            builder.row(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'prefered#$channel#${j["id"]}'))
        else:
            builder.add(types.InlineKeyboardButton(text=f'{i+1}',callback_data=f'prefered#$channel#${j["id"]}'))
    return builder.as_markup()
    

def choose_channel_rkt(channels):
    if channels==None:
        return None
    builder = ReplyKeyboardBuilder()
    # print("choose_channel_rkt")
    # print(channels)
    for i,j in enumerate(channels):
        if i%5<1:

            builder.row(types.KeyboardButton(text=f"{i+1}"))  
        else:
            builder.add(types.KeyboardButton(text=f"{i}"))
    return builder.as_markup(resize_keyboard=True)


def yes_no_admin_ikt(lang,id,ad_type):
    data={"uzb":["Ha","Yo'q"],"rus":["Да","Нет"]}[lang]
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text=data[0],callback_data=f"admin#$confirm#${id}%{ad_type}%yes"),
                types.InlineKeyboardButton(text=data[1],callback_data=f"admin#$confirm#${id}%{ad_type}%no"))
    return builder.as_markup()

def back_to_the_past_ikt(lang):
    we={"uzb":"Orqaga","rus":"Назад"}[lang]
    builder=InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text=f'{we}',callback_data=f'back#$to#$the#$past'))
    return builder.as_markup()
