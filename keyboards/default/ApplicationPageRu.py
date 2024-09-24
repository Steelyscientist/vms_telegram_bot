from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

application_page_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Анонимное обращение"),
            KeyboardButton(text="Открытое обращение")
        ],
        [
            KeyboardButton(text="назад к Меню"),
        ],
    ],
    resize_keyboard=True
)

phone_and_location_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона", request_contact=True),
        ],
        [
            KeyboardButton(text="Отправить местоположение", request_location=True),
        ],
    ],
    resize_keyboard=True
)