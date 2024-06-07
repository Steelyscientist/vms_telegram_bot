from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Javob berish / Отвечать"),
        ],
        [
            KeyboardButton(text="Ortga / Назад"),
        ]
    ],
    resize_keyboard=True
)