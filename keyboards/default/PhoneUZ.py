from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kontaktni ulashish", request_contact=True),
        ],
        [
            KeyboardButton(text="Menyuga qaytish"),
        ]
    ],
    resize_keyboard=True
)