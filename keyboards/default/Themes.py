from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

app_theme_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сексуальное насилие"),
            KeyboardButton(text="Домашнее насилие"),
        ],
        [
            KeyboardButton(text="Буллинг"),
            KeyboardButton(text="Суицид"),
        ],
        [
            KeyboardButton(text="Беременность"),
            KeyboardButton(text="Химическая зависимость"),
        ],
        # [
        #     KeyboardButton(text="Открытое обращение"),
        #     KeyboardButton(text="Открытое обращение"),
        # ],
    ],
    resize_keyboard=True,
)

app_theme_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Jinsiy zo'ravonlik"),
            KeyboardButton(text="Oiladagi zo'ravonlik"),
        ],
        [
            KeyboardButton(text="Bulling"),
            KeyboardButton(text="Suitsid"),
        ],
        [
            KeyboardButton(text="Homiladorlik"),
            KeyboardButton(text="Giyohvandlik"),
        ],
    ],
    resize_keyboard=True,
)

app_intrest_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Хочу больше информации по теме"),
        ],
        [
            KeyboardButton(text="Мне срочно нужна помощь"),
        ],
    ],
    resize_keyboard=True,
)

app_intrest_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mavzuga ko'proq ma'lumot kerak"),
        ],
        [
            KeyboardButton(text="Menga tez yordam kerak"),
        ],
    ],
    resize_keyboard=True,
)
