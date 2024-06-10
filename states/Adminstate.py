from aiogram.dispatcher.filters.state import StatesGroup, State


class adminstate(StatesGroup):
    ansver = State()
    userid = State()
    confirm = State()
    statistics = State()
