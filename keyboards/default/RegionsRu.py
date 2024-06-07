from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

regions_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Республика Каракалпакстан"),
            KeyboardButton(text="Андижанская область")
        ],
        [
            KeyboardButton(text="Бухарская область"),
            KeyboardButton(text="Ферганская област")
        ],
        [
            KeyboardButton(text="Джизакская область"),
            KeyboardButton(text="Хорезмская область")
        ],
        [
            KeyboardButton(text="Наманганская область"),
            KeyboardButton(text="Навоийская область")
        ],
        [
            KeyboardButton(text="Кашкадарьинская область"),
            KeyboardButton(text="Самаркандская область")
        ],
        [
            KeyboardButton(text="Сырдарьинская область"),
            KeyboardButton(text="Сурхандарьинская область")
        ],
        [
            KeyboardButton(text="Ташкентская область"),
            KeyboardButton(text="город Ташкент")
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True
)