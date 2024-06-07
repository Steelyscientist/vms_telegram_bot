from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.SelectLanguage import start
from keyboards.default.RegionsRu import regions_ru
from keyboards.default.RegionsUz import regions_uz
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart(), state=appstate.pol_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

@dp.message_handler(CommandStart(), state=appstate.pol_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


def is_region_only(text):
    return all("Erkak" or "Ayol" or  "Мужчина" or "Женщина" in text)


@dp.message_handler(text="Ortga", state = appstate.pol_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Qaysi hududda istiqomat qilasiz?", reply_markup=regions_uz)
    await appstate.region_uz.set()

@dp.message_handler(text="Назад", state = appstate.pol_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("В каком регионе вы живете?", reply_markup=regions_ru)
    await appstate.region_ru.set()


@dp.message_handler(text="Erkak", state = appstate.pol_uz)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_region_only(message.text):
            user_pol = message.text
            await state.update_data(
                {
                    "Jinsi": user_pol,
                }
            )
            await message.answer(text="Murojaat matnini kiriting", reply_markup=psychologist_page_uz)
            await appstate.app_tex_uz.set()
        else:
            await message.reply("Iltimos, faqat tugmalardan birini bosing.")
    else:
        await message.reply("Iltimos, faqat tugmalardan birini bosing.")

@dp.message_handler(text="Ayol", state = appstate.pol_uz)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_region_only(message.text):
            user_pol = message.text
            await state.update_data(
                {
                    "Jinsi": user_pol,
                }
            )
            await message.answer(text="Murojaat matnini kiriting", reply_markup=psychologist_page_uz)
            await appstate.app_tex_uz.set()
        else:
            await message.reply("Iltimos, faqat tugmalardan birini bosing.")
    else:
        await message.reply("Iltimos, faqat tugmalardan birini bosing.")



@dp.message_handler(text="Мужчина", state=appstate.pol_ru)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_region_only(message.text):
            user_pol = message.text
            await state.update_data(
                {
                    "Jinsi": user_pol,
                }
            )
            await message.answer(text="Введите текст обращения", reply_markup=psychologist_page_ru)
            await appstate.app_tex_ru.set()
        else:
            await message.reply("Пожалуйста, нажмите только одну из кнопок.")
    else:
        await message.reply("Пожалуйста, нажмите только одну из кнопок.")


@dp.message_handler(text="Женщина", state=appstate.pol_ru)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_region_only(message.text):
            user_pol = message.text
            await state.update_data(
                {
                    "Jinsi": user_pol,
                }
            )
            await message.answer(text="Введите текст обращения", reply_markup=psychologist_page_ru)
            await appstate.app_tex_ru.set()
        else:
            await message.reply("Пожалуйста, нажмите только одну из кнопок.")
    else:
        await message.reply("Пожалуйста, нажмите только одну из кнопок.")

