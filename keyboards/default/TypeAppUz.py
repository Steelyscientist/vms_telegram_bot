from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

type_app_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Gaplashishni istayman"),
        KeyboardButton(text="Murojaat qoldirish")
        ],
        [
            KeyboardButton(text="Ortga"),
        ],
    ],
    resize_keyboard=True
)