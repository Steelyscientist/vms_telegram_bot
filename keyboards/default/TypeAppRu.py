from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

type_app_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Запишитесь на консультацию Психолога"),
        KeyboardButton(text="Оставить заявку")
        ],
        [
        KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True
)