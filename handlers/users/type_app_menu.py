from aiogram import types
from loader import dp
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards.default.SelectLanguage import start
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.ApplicationPageRu import application_page_ru
from keyboards.default.ApplicationPageUz import application_page_uz
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.PhoneUZ import phone_uz
from keyboards.default.PhoneRU import phone_ru

@dp.message_handler(CommandStart(), state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

@dp.message_handler(text="Ortga", state = appstate.type_block )
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Назад", state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Psixolog maslaxatiga yozilish", state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    modul = message.text
    username = message.from_user.username
    if username:
        user_info = f"@{username}"
    else:
        user_info = "mavjud emas"

    await state.update_data(
        {
            "Ism": name,
            "Nick name": user_info,
            "UserID": user_id,
            "Modul": modul,
        }
    )
    await message.answer("Iltimos, tugma yordamida kontakt ma'lumotlaringizni yuboring.",reply_markup=phone_uz)
    await appstate.phone_uz.set()


@dp.message_handler(text="Запишитесь на консультацию Психолога", state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    modul = message.text
    username = message.from_user.username
    if username:
        user_info = f"@{username}"
    else:
        user_info = "mavjud emas"

    await state.update_data(
        {
            "Ism": name,
            "Nick name": user_info,
            "UserID": user_id,
            "Modul": modul,
        }
    )
    await message.answer("Пожалуйста, поделитесь своей контактной информацией, используя кнопку.", reply_markup=phone_ru)
    await appstate.phone_ru.set()


@dp.message_handler(text="Murojaat qoldirish", state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    modul = message.text
    username = message.from_user.username
    if username:
        user_info = f"@{username}"
    else:
        user_info = "mavjud emas"
    await state.update_data(
        {
            "Ism": name,
            "Nick name": user_info,
            "UserID": user_id,
            "Modul": modul,
         }
    )
    await message.answer("Murojaat turini tanlang", reply_markup=application_page_uz)
    await appstate.type_app.set()


@dp.message_handler(text="Оставить заявку", state = appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    modul = message.text
    username = message.from_user.username
    if username:
        user_info = f"@{username}"
    else:
        user_info = "mavjud emas"

    await state.update_data(
        {
            "Ism": name,
            "Nick name": user_info,
            "UserID": user_id,
            "Modul": modul,
         }
    )
    await message.answer("Выберите тип обращения.", reply_markup=application_page_ru)
    await appstate.type_app.set()


