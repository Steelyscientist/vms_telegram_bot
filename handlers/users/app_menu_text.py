from aiogram import types
from loader import dp, bot, db
from data.config import GROUP_ID, ADMINS
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.SelectLanguage import start
from keyboards.default.PolRu import pol_page_ru
from keyboards.default.PolUz import pol_page_uz
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
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type:
        await message.answer("Jinsingizni belgilang.", reply_markup=pol_page_uz)
        await appstate.pol_uz.set()
    else:
        await message.answer("Bo'limni tanlang", reply_markup=type_app_uz)
        await appstate.type_block.set()


@dp.message_handler(text="назад к Меню", state=appstate.app_tex_ru)
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type:
        await message.answer("Укажите свой пол.", reply_markup=pol_page_ru)
        await appstate.pol_ru.set()
    else:
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
            age = data.get("Yosh")
            username = data.get("Nick name") if data.get("Nick name") else message.from_user.first_name
            user_id = data.get("UserID") if data.get("UserID") else message.from_user.id
            phone = data.get("Nomer")
            modul = data.get("Modul")
            theme = data.get("Theme")
            app_type = data.get("Turkum")
            Uztext = data.get("Matin")

            if app_type == "Anonim murojaat":
                appeal_id = db.create_appeal(
                    user_id=user_id,
                    text=Uztext,
                    type="Anonymous",
                    status=1,
                    theme=modul,
                )
                msg5 = f"<b>Appeal ID:</b> {appeal_id}\n<b>User ID:</b> {user_id}\n<b>Username:</b> {username}\n<b>Murojaat turi:</b> {app_type}\n<b>Murojaat:</b>\n{Uztext}"
                await message.answer(
                    "Sizning murojaatingiz qabul qilindi. Tez fursatda mutaxassis javobini kuting. Zaruriyat bo'lgan taqdirda Zoom orqali maslahat olishingiz uchun havola jo'natiladi.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg5)
                await appstate.wait_answer.set()
            elif app_type == "Ochiq murojaat":
                appeal_id = db.create_appeal(
                    user_id=user_id, text=Uztext, type="Open", status=1, theme=theme
                )
                msg6 = f"<b>Appeal ID:</b> {appeal_id}\n<b>User ID:</b> {user_id}<b>Ism:</b> {name}\n<b>Yosh:</b> {age}\n<b>Nick name:</b> {username}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat turi:</b> {app_type}\n<b>Mavzu: </b>{theme}\n<b>Murojaat:</b>\n{Uztext}"
                await message.answer(
                    "Sizning murojaatingiz qabul qilindi. Tez fursatda mutaxassis javobini kuting. Zaruriyat bo'lgan taqdirda Zoom orqali maslahat olishingiz uchun havola jo'natiladi.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg6)
                await appstate.wait_answer.set()
            else:
                msg3 = f"<b>Ism:</b> {name}\n<b>Nick name:</b> {username}\n<b>User ID:</b> {user_id}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat:</b>\n{Uztext}"
                await message.answer(
                    "Sizning murojaatingiz qabul qilindi. Tez fursatda mutaxassis javobini kuting. Zaruriyat bo'lgan taqdirda Zoom orqali maslahat olishingiz uchun havola jo'natiladi.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg3)
                await appstate.wait_answer.set()

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
            age = data.get("Yosh")
            username = data.get("Nick name") if data.get("Nick name") else message.from_user.first_name
            user_id = data.get("UserID") if data.get("UserID") else message.from_user.id
            phone = data.get("Nomer")
            modul = data.get("Modul")
            theme = data.get("Theme")
            app_type = data.get("Turkum")
            Rutext = data.get("Matin")

            if app_type == "Анонимное обращение":
                appeal_id = db.create_appeal(
                    user_id=user_id,
                    text=Rutext,
                    type="Anonymous",
                    status=1,
                    theme=modul,
                )
                msg5 = f"<b>Appeal ID:</b> {appeal_id}\n<b>User ID:</b> {user_id}\n<b>Username:</b> {username}\n<b>Murojaat turi:</b> {app_type}\n<b>Murojaat:</b>\n{Rutext}"
                await message.answer(
                    "Ваше обращение принято. Ожидайте ответа специалиста в ближайшее время. В случае необходимости будет отправлена ссылка для консультации через Zoom.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg5)
                await appstate.wait_answer.set()
            elif app_type == "Открытое обращение":
                appeal_id = db.create_appeal(
                    user_id=user_id, text=Rutext, type="Open", status=1, theme=theme
                )
                msg6 = f"<b>Appeal ID:</b> {appeal_id}\n<b>Ism:</b> {name}\n<b>Yosh:</b> {age}\n<b>Nick name:</b> {username}\n<b>User ID:</b> {user_id}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat turi:</b> {app_type}\n<b>Mavzu: </b>{theme}\n<b>Murojaat:</b>\n{Rutext}"
                await message.answer(
                    "Ваше обращение принято. Ожидайте ответа специалиста в ближайшее время. В случае необходимости будет отправлена ссылка для консультации через Zoom.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg6)
                await appstate.wait_answer.set()
            else:
                msg4 = f"<b>Ism:</b> {name}\n<b>Nick name:</b> {username}\n<b>User ID:</b> {user_id}\n<b>Telefon:</b> {phone}\n<b>Modul:</b> {modul}\n<b>Murojaat:</b>\n{Rutext}"
                await message.answer(
                    "Ваше обращение принято. Ожидайте ответа специалиста в ближайшее время. В случае необходимости будет отправлена ссылка для консультации через Zoom.",
                    reply_markup=None,
                )
                await bot.send_message(ADMINS[0], text=msg4)
                await appstate.wait_answer.set()
        else:
            await message.reply(
                "Пожалуйста, отправляйте только текст. Другие виды информации не принимаются."
            )
    else:
        await message.reply(
            "Пожалуйста, отправляйте только текст. Другие виды информации не принимаются."
        )


@dp.message_handler(content_types=types.ContentType.ANY, state=appstate.wait_answer)
async def wait_answer(message: types.Message):
    print(message)
    user_id = message.from_user.id
    msg = f"<b>User ID:</b> {user_id}\n<b>Username:</b> {message.from_user.first_name}\n{message.text}"
    appeals = db.get_appeals_by_user_id(user_id)
    appeal_id = appeals[-1][0]

    admin_id = int(ADMINS[0])
    replies = db.get_replies_by_appeal_id_and_user_id(user_id=admin_id, appeal_id=appeal_id)

    db.create_reply(appeal_id=appeal_id, user_id=user_id, text=message.text, reply_id=replies[0][0])

    await bot.send_message(ADMINS[0], text=msg, reply_to_message_id=replies[0][5])
    await appstate.wait_answer.set()
