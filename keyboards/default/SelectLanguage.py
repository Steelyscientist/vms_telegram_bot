from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbekcha"),
            KeyboardButton(text="Русский")
        ],
    ],
    resize_keyboard=True
)
