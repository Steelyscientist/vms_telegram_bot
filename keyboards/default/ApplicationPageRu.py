from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

application_page_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Анонимное обращение"),
            KeyboardButton(text="Открытое обращение")
        ],
        [
            KeyboardButton(text="назад к Меню"),
        ],
    ],
    resize_keyboard=True
)