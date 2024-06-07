from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.TypeAppUz import type_app_uz
from keyboards.default.TypeAppRu import type_app_ru
from keyboards.default.RegionsRu import regions_ru
from keyboards.default.RegionsUz import regions_uz
from keyboards.default.PhoneUZ import phone_uz
from keyboards.default.PhoneRU import phone_ru
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher.filters.builtin import CommandStart

@dp.message_handler(CommandStart(), state=appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()

@dp.message_handler(text="Menyuga qaytish", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang", reply_markup=type_app_uz)
    await appstate.type_block.set()

@dp.message_handler(text="назад к Меню", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Выберите раздел", reply_markup=type_app_ru)
    await appstate.type_block.set()

@dp.message_handler(text="Анонимное обращение", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    app_type = message.text
    await state.update_data(
        {
            "Turkum": app_type,
        }
    )

    await message.answer("В каком регионе вы живете?", reply_markup=regions_ru)
    await appstate.region_ru.set()


@dp.message_handler(text="Anonim murojaat", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    app_type = message.text
    await state.update_data(
        {
            "Turkum": app_type,
        }
    )

    await message.answer("Qaysi hududda istiqomat qilasiz?", reply_markup=regions_uz)
    await appstate.region_uz.set()

@dp.message_handler(text="Открытое обращение", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    app_type = message.text
    await state.update_data(
        {
            "Turkum": app_type,
        }
    )
    await message.answer("Пожалуйста, поделитесь своей контактной информацией, используя кнопку.", reply_markup=phone_ru)
    await appstate.phone_ru.set()

@dp.message_handler(text="Ochiq murojaat", state = appstate.type_app)
async def bot_start(message: types.Message, state: FSMContext):
    app_type = message.text
    await state.update_data(
        {
            "Turkum": app_type,
        }
    )
    await message.answer("Iltimos, tugma yordamida kontakt ma'lumotlaringizni yuboring.", reply_markup=phone_uz)
    await appstate.phone_uz.set()




