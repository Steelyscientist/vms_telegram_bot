from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.RegionsRu import regions_ru
from keyboards.default.RegionsUz import regions_uz
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher.filters.builtin import CommandStart

@dp.message_handler(CommandStart(), state=appstate.age_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

@dp.message_handler(CommandStart(), state=appstate.age_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

def is_numbers_only(text):
    return all(char.isdigit() for char in text)

@dp.message_handler(text="Menyuga qaytish", state = appstate.age_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Ism familiyangiz.", reply_markup=psychologist_page_uz)
    await appstate.fullname_uz.set()

@dp.message_handler(text="назад к Меню", state = appstate.age_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Ваше имя и фамилия.", reply_markup=psychologist_page_ru)
    await appstate.fullname_ru.set()

@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.age_uz)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_numbers_only(message.text):
            user_age = message.text

            await state.update_data(
                {
                    "Yosh": user_age,
                }
            )
            await message.answer("Qaysi hududda istiqomat qilasiz?", reply_markup=regions_uz)
            await appstate.region_uz.set()
        else:
            await message.reply("Iltimos, faqat raqam yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.")
    else:
        await message.reply("Iltimos, faqat raqam yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.")


@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.age_ru)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_numbers_only(message.text):
            user_age = message.text

            await state.update_data(
                {
                    "Yosh": user_age,
                }
            )
            await message.answer("В каком регионе вы живете?", reply_markup=regions_ru)
            await appstate.region_ru.set()
        else:
            await message.reply("Пожалуйста, отправьте только цифры. Другая информация не принимается")
    else:
        await message.reply("Пожалуйста, отправьте только цифры. Другая информация не принимается")





