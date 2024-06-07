from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

psychologist_page_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="назад к Меню"),
        ],
    ],
    resize_keyboard=True
)