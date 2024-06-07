import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.AdminPanelUz import admin_uz
from states.Adminstate import adminstate
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher import FSMContext
from keyboards.default.Canclebutton import cancle_btn

from aiogram.dispatcher.filters.builtin import CommandStart

@dp.message_handler(CommandStart(), state = adminstate)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()
def is_text_and_numbers_only(text):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~ абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ")
    return all(char in allowed_chars for char in text)

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/post", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Botdagi o'zgarishlar bo'ldi, qayta ishga tushirish uchun /start tugmasini bosib yuboring \n\nБот изменился, нажмите /start для перезапуска")
        await asyncio.sleep(0.05)


@dp.message_handler(text="Ortga / Назад", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=start)

@dp.message_handler(text="Javob berish / Отвечать", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer("Matnini kiriting / Введите текст", reply_markup=cancle_btn)
    await adminstate.ansver.set()

@dp.message_handler(text="Bekor qilish / Отмена", user_id=ADMINS, state = adminstate.ansver)
async def bot_answer_cancle(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)
    await state.finish()

@dp.message_handler(content_types=types.ContentType.ANY, user_id=ADMINS, state = adminstate.ansver)
async def bot_answer_text(message: types.Message, state: FSMContext):
    operator_id = message.from_user.id
    if message.content_type == 'text':
        if is_text_and_numbers_only(message.text):

            text_uz = message.text

            await state.update_data(
                {
                    "Matin": text_uz,
                    "Operator" : operator_id,
                }
            )
            await message.answer("Arizachining Telegram ID sini kriting / Введите Telegram ID заявителя", reply_markup=cancle_btn)
            await adminstate.userid.set()
        else:
            await message.reply("Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.\n\nПожалуйста, отправляйте только текст. Другие виды информации не принимаются.")
    else:
        await message.reply("Iltimos, faqat matn yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.\n\nПожалуйста, отправляйте только текст. Другие виды информации не принимаются.")


@dp.message_handler(text="Bekor qilish / Отмена", user_id=ADMINS, state = adminstate.userid)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)
    await state.finish()

def is_numbers_only(text):
    return all(char.isdigit() for char in text)

@dp.message_handler(content_types=types.ContentType.ANY, user_id=ADMINS, state = adminstate.userid)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_numbers_only(message.text):
            ID = int(message.text)
            userid = db.select_user(id=ID)
            if userid:
                await state.update_data(
                    {
                        "ID": userid,
                    }
                )
                await message.answer("Javobni yuborishini tasdiqlash uchun <b>Tasdiqlayman</b> jumlasini yuboring \n\n Отправьте <b>Подтверждаю</b>,чтобы подтвердить отправку ответа.", reply_markup=cancle_btn)
                await adminstate.confirm.set()
            else:
                await message.reply(f"Foydalanuvchi ID raqami: {ID} noto'g'ri.\n\nИдентификатор пользователя: {ID} недействителен.")
        else:
            await message.reply("Iltimos, faqat raqam yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.\n\nПожалуйста, отправьте только цифры. Другая информация не принимается")
    else:
        await message.reply("Iltimos, faqat raqam yuboring. Boshqa turdagi ma'lumotlar qabul qilinmaydi.\n\nПожалуйста, отправьте только цифры. Другая информация не принимается")

@dp.message_handler(text="Bekor qilish / Отмена", user_id=ADMINS, state = adminstate.confirm)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Bo'limni tanlang / Выберите раздел", reply_markup=admin_uz)
    await state.finish()
def is_confirm_only(text):
    return all("Tasdiqlayman" or "Подтверждаю" in text)

@dp.message_handler(content_types=types.ContentType.ANY, user_id=ADMINS, state = adminstate.confirm)
async def bot_start(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        if is_confirm_only(message.text):
            confirm = message.text

            await state.update_data(
                {
                    "Confirm": confirm,
                }
            )
            data = await state.get_data()
            user_id = data.get("ID")
            operator = data.get("Operator")
            Uztext = data.get("Matin")
            msg8 = f"<b>Operator ID:</b> {operator}\n\n{Uztext}"
            await message.answer(
                f"Murojattga javobingiz {user_id[0]} raqamli foydalanuvchiga yuborildi \n\nВаш ответ отправлен пользователю {user_id[0]}.",
                reply_markup=start)
            userid = db.select_user(id=user_id[0])

            await bot.send_message(chat_id=userid[0], text=msg8)
            await state.finish()
        else:
            await message.reply("Iltimos harakatingizni tasdiqlang\n\nПожалуйста, подтвердите свое действие")
    else:
        await message.reply("Iltimos harakatingizni tasdiqlang\n\nПожалуйста, подтвердите свое действие")

@dp.message_handler(text="/cleandb", user_id=ADMINS,)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")