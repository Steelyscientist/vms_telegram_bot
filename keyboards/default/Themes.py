from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

app_theme_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Анонимное обращение"),
            KeyboardButton(text="Открытое обращение"),
        ],
        [
            KeyboardButton(text="назад к Меню"),
        ],
    ],
    resize_keyboard=True,
)

app_theme_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Анонимное обращение"),
            KeyboardButton(text="Открытое обращение"),
        ],
        [
            KeyboardButton(text="назад к Меню"),
        ],
    ],
    resize_keyboard=True,
)
