from aiogram import types

from loader import dp
from states.Appstate import appstate


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(text = "Buyruqlardan birini tanlang / Выберите одну из команд")


@dp.message_handler(state=appstate.type_block)
async def bot_echo(message: types.Message):
    await message.answer(text = "Buyruqlardan birini tanlang / Выберите одну из команд")

@dp.message_handler(state=appstate.type_app)
async def bot_echo(message: types.Message):
    await message.answer(text="Buyruqlardan birini tanlang / Выберите одну из команд")



