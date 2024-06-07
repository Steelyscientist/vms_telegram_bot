from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделиться контактом", request_contact=True),
        ],
        [
            KeyboardButton(text="назад к Меню"),
        ]
    ],
    resize_keyboard=True
)