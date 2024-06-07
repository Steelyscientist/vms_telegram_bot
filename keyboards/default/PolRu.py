from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pol_page_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мужчина"),
            KeyboardButton(text="Женщина")
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True
)