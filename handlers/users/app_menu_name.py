from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.ApplicationPageRu import application_page_ru
from keyboards.default.ApplicationPageUz import application_page_uz
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher.filters.builtin import CommandStart

@dp.message_handler(CommandStart(), state=appstate.fullname_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

@dp.message_handler(CommandStart(), state=appstate.fullname_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

def is_text_only(text):
    return all(char.isalpha() or char.isspace() for char in text)

@dp.message_handler(text="Menyuga qaytish", state = appstate.fullname_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang", reply_markup=application_page_uz)
    await appstate.type_app.set()

@dp.message_handler(text="назад к Меню", state = appstate.fullname_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Выберите раздел", reply_markup=application_page_ru)
    await appstate.type_app.set()

@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.fullname_uz)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_text_only(message.text):
            full_name = message.text

            await state.update_data(
                {
                    "Ism": full_name,
                }
            )
            await message.answer("Yoshingiz", reply_markup=psychologist_page_uz)
            await appstate.age_uz.set()
        else:
            await message.reply("Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.")
    else:
        await message.reply("Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.")


@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.fullname_ru)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_text_only(message.text):
            full_name = message.text

            await state.update_data(
                {
                    "Ism": full_name,
                }
            )
            await message.answer("Ваш возраст", reply_markup=psychologist_page_ru)
            await appstate.age_ru.set()
        else:
            await message.reply("Пожалуйста, отправляйте только текст. Другие виды информации не принимаются.")
    else:
        await message.reply("Пожалуйста, отправляйте только текст. Другие виды информации не принимаются.")





