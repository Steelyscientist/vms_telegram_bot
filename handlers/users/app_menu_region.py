from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.ApplicationPageRu import application_page_ru
from keyboards.default.ApplicationPageUz import application_page_uz
from keyboards.default.PolRu import pol_page_ru
from keyboards.default.PolUz import pol_page_uz
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart(), state=appstate.region_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(CommandStart(), state=appstate.region_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

def is_region_only(text):
    return all("Республика Каракалпакстан" or "Андижанская область" or "Бухарская область" or "Ферганская област" or "Джизакская область" or "Хорезмская область" or "Наманганская область" or "Навоийская область" or "Кашкадарьинская область" or "Самаркандская область" or "Сырдарьинская область" or "Сурхандарьинская область" or "Ташкентская область" or "город Ташкент" or "Qoraqalpogʻiston Respublikasi" or "Andijon viloyati" or "Buxoro viloyati" or "Fargʻona viloyati" or "Jizzax viloyati" or "Xorazm viloyati" or "Namangan viloyati" or "Navoiy viloyati" or "Qashqadaryo viloyati" or "Samarqand viloyati" or "Sirdaryo viloyati" or "Surxondaryo viloyati" or "Toshkent viloyati" or "Toshkent shaxri" in text)

@dp.message_handler(text="Ortga", state = appstate.region_uz)
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type == "Anonim murojaat":

        await message.answer("Bo'limni tanlang", reply_markup=application_page_uz)
        await appstate.type_app.set()
    else:
        await message.answer("Yoshingiz", reply_markup=psychologist_page_uz)
        await appstate.age_uz.set()

@dp.message_handler(text="Назад", state = appstate.region_ru)
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type == "Анонимное обращение":

        await message.answer("Выберите раздел", reply_markup=application_page_ru)
        await appstate.type_app.set()
    else:
        await message.answer("Ваш возраст", reply_markup=psychologist_page_ru)
        await appstate.age_ru.set()

@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.region_uz)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_region_only(message.text):
            user_region = message.text

            await state.update_data(
                {
                    "Hudud": user_region,
                }
            )
            await message.answer("Jinsingizni belgilang.", reply_markup=pol_page_uz)
            await appstate.pol_uz.set()
        else:
            await message.reply("Iltimos, faqat menyudagi hududlardan birini tanlang.")
    else:
        await message.reply("Iltimos, faqat menyudagi hududlardan birini tanlang.")


@dp.message_handler(content_types=types.ContentType.ANY, state = appstate.region_ru)
async def bot_start(message: types.Message, state: FSMContext):

    if message.content_type == 'text':
        if is_region_only(message.text):
            user_region = message.text

            await state.update_data(
                {
                    "Hudud": user_region,
                }
            )
            await message.answer("Укажите свой пол.", reply_markup=pol_page_ru)
            await appstate.pol_ru.set()
        else:
            await message.reply("Пожалуйста, выберите только один из пунктов меню.")
    else:
        await message.reply("Пожалуйста, выберите только один из пунктов меню.")





