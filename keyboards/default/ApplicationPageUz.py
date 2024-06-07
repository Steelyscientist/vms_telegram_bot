from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

application_page_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Anonim murojaat"),
            KeyboardButton(text="Ochiq murojaat")
        ],
        [
            KeyboardButton(text="Menyuga qaytish"),
        ],
    ],
    resize_keyboard=True
)