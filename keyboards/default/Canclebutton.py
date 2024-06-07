from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancle_btn = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Bekor qilish / Отмена"),
        ],
    ],
    resize_keyboard=True
)