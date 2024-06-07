from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.SelectLanguage import start
from keyboards.default.TypeAppUz import type_app_uz
from keyboards.default.TypeAppRu import type_app_ru
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart(), state=appstate.app_tex_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(CommandStart(), state=appstate.app_tex_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


def is_text_and_numbers_only(text):
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~ абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    )
    return all(char in allowed_chars for char in text)


@dp.message_handler(text="Menyuga qaytish", state=appstate.app_tex_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang", reply_markup=type_app_uz)
    await appstate.type_block.set()


@dp.message_handler(text="назад к Меню", state=appstate.app_tex_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Выберите раздел", reply_markup=type_app_ru)
    await appstate.type_block.set()


@dp.message_handler(content_types=types.ContentType.ANY, state=appstate.app_tex_uz)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == "text":
        if is_text_and_numbers_only(message.text):
            text_uz = message.text

            await state.update_data(
                {
                    "Matin": text_uz,
                }
            )
            data = await state.get_data()
            name = data.get("Ism")
            username = data.get("Nick name")
            user_id = data.get("UserID")
            phone = data.get("Nomer")
            modul = data.get("Modul")
            Uztext = data.get("Matin")
            msg3 = f"<b>Ism:</b> {name}\n<b>Nick name:</b> {username}\n<b>User ID:</b> {user_id}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat:</b>\n{Uztext}"
            await message.answer(
                "Sizning murojaatingiz qabul qilindi. Tez fursatda mutaxassis javobini kuting. Zaruriyat bo'lgan taqdirda Zoom orqali maslahat olishingiz uchun havola jo'natiladi.",
                reply_markup=start,
            )
            await bot.send_message(-1002176563327, text=msg3)
            await state.finish()
        else:
            await message.reply(
                "Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi."
            )
    else:
        await message.reply(
            "Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi."
        )


@dp.message_handler(content_types=types.ContentType.ANY, state=appstate.app_tex_ru)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == "text":
        if is_text_and_numbers_only(message.text):
            text_ru = message.text
            await state.update_data(
                {
                    "Matin": text_ru,
                }
            )
            data = await state.get_data()
            name = data.get("Ism")
            username = data.get("Nick name")
            user_id = data.get("UserID")
            phone = data.get("Nomer")
            modul = data.get("Modul")
            Rutext = data.get("Matin")
            msg4 = f"<b>Ism:</b> {name}\n<b>Nick name:</b> {username}\n<b>User ID:</b> {user_id}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat:</b>\n{Rutext}"
            await message.answer(
                "Ваше обращение принято. Ожидайте ответа специалиста в ближайшее время. В случае необходимости будет отправлена ссылка для консультации через Zoom.",
                reply_markup=start,
            )
            await bot.send_message(-1002176563327, text=msg4)
            await state.finish()
        else:
            await message.reply(
                "Пожалуйста, отправляйте только текст. Другие виды информации не принимаются."
            )
    else:
        await message.reply(
            "Пожалуйста, отправляйте только текст. Другие виды информации не принимаются."
        )
