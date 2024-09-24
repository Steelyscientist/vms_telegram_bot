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

phone_and_location_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni yuborish", request_contact=True),
        ],
        [
            KeyboardButton(text="Joylashuvni yuborish", request_location=True),
        ],
    ],
    resize_keyboard=True
)