from aiogram.dispatcher.filters.state import StatesGroup, State


class appstate(StatesGroup):
    type_block = State()
    type_app = State()
    app_theme = State()
    app_interest = State()
    phone_uz = State()
    phone_ru = State()
    fullname_uz = State()
    fullname_ru = State()
    age_uz = State()
    age_ru = State()
    region_uz = State()
    region_ru = State()
    pol_uz = State()
    pol_ru = State()
    app_tex_uz = State()
    app_tex_ru = State()
