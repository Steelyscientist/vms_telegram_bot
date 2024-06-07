from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pol_page_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Erkak"),
            KeyboardButton(text="Ayol")
        ],
        [
            KeyboardButton(text="Ortga"),
        ],
    ],
    resize_keyboard=True
)