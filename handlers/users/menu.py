from aiogram import types
from loader import dp, db
from aiogram.dispatcher import FSMContext
from keyboards.default.TypeAppUz import type_app_uz
from keyboards.default.TypeAppRu import type_app_ru
from states.Appstate import appstate
from data.config import ADMINS
from data.config import OPERATOR
from keyboards.default.AdminPanelUz import admin_uz


@dp.message_handler(text="O'zbekcha")
async def bot_start(message: types.Message):
    db.update_user_language(id=message.from_user.id, language="uz")
    await message.answer("Bo'limni tanlang", reply_markup=type_app_uz)
    await appstate.type_block.set()


@dp.message_handler(text="Русский")
async def bot_start(message: types.Message):
    db.update_user_language(id=message.from_user.id, language="ru")
    await message.answer("Выберите раздел", reply_markup=type_app_ru)
    await appstate.type_block.set()


@dp.message_handler(
    text="/admin",
    user_id=ADMINS,
)
async def bot_start(message: types.Message):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)


@dp.message_handler(text="/admin", user_id=OPERATOR)
async def bot_start(message: types.Message):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)


@dp.message_handler(text="/admin", user_id=ADMINS, state=appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)
    await state.finish()


@dp.message_handler(text="/admin", user_id=OPERATOR, state=appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)
    await state.finish()
