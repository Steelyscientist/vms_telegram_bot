from aiogram import types
from aiogram.types import ContentType

from loader import dp, db
from aiogram.dispatcher import FSMContext
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.TypeAppUz import type_app_uz
from keyboards.default.TypeAppRu import type_app_ru
from keyboards.default.ApplicationPageRu import application_page_ru
from keyboards.default.ApplicationPageUz import application_page_uz
from keyboards.default.SelectLanguage import start
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart(), state=appstate.phone_uz)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(CommandStart(), state=appstate.phone_ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Menyuga qaytish", state=appstate.phone_uz)
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type:
        if app_type == "Ochiq murojaat":
            await message.answer(
                "Murojaat turini tanlang", reply_markup=application_page_uz
            )
            await appstate.type_app.set()
    else:
        await message.answer("Bo'limni tanlang", reply_markup=type_app_uz)
        await appstate.type_block.set()


@dp.message_handler(text="назад к Меню", state=appstate.phone_ru)
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    app_type = data.get("Turkum")
    if app_type:
        if app_type == "Открытое обращение":
            await message.answer(
                "Выберите тип обращения.", reply_markup=application_page_ru
            )
            await appstate.type_app.set()
    else:
        await message.answer("Выберите раздел", reply_markup=type_app_ru)
        await appstate.type_block.set()


@dp.message_handler(content_types=ContentType.CONTACT, state=appstate.phone_uz)
async def contact_handler(message: types.Message, state: FSMContext):
    contact = message.contact
    data = await state.get_data()
    app_type = data.get("Turkum")

    # Check if the contact has a valid phone number
    if contact.phone_number:
        # update user data with the phone number
        db.update_user_phone(id=message.from_user.id, phone=contact.phone_number)
        if app_type:
            if app_type == "Ochiq murojaat":
                await state.update_data(
                    {
                        "Nomer": contact["phone_number"],
                    }
                )
                await message.answer(
                    "Ism familiyangiz.", reply_markup=psychologist_page_uz
                )
                await appstate.fullname_uz.set()
        else:
            db.create_appeal(
                message.from_user.id, contact["phone_number"], "Consultation", 1
            )
            await state.update_data(
                {
                    "Nomer": contact["phone_number"],
                }
            )
            msg2 = f"Hurmatli {message.from_user.full_name}!\n Siz o'zingizni qiynayotgan muammoli vaziyat yuzasidan psixolog maslahatiga yozilishingiz va psixolog bilan Zoom uchrashuvi orqali maslahat olishingiz mumkin. iltimos maslahat olmoqchi bo'lgan muammoli vaziyat haqida batafsil yozing."
            await message.answer(text=msg2, reply_markup=psychologist_page_uz)
            await appstate.app_tex_uz.set()

    else:
        await message.answer(
            "Iltimos, tugma yordamida kontakt ma'lumotlaringizni yuboring."
        )


@dp.message_handler(state=appstate.phone_uz)
async def handle_invalid_contact(message: types.Message, state: FSMContext):
    # If the user sends something other than a contact
    await message.answer(
        "Iltimos, tugma yordamida kontakt ma'lumotlaringizni baham ko'ring."
    )


@dp.message_handler(content_types=ContentType.CONTACT, state=appstate.phone_ru)
async def contact_handler(message: types.Message, state: FSMContext):
    contact = message.contact
    data = await state.get_data()
    app_type = data.get("Turkum")

    # Check if the contact has a valid phone number
    if contact.phone_number:
        # update user data with the phone number
        db.update_user_phone(id=message.from_user.id, phone=contact.phone_number)
        if app_type:
            if app_type == "Открытое обращение":
                await state.update_data(
                    {
                        "Nomer": contact["phone_number"],
                    }
                )
                await message.answer(
                    "Ваше имя и фамилия.", reply_markup=psychologist_page_ru
                )
                await appstate.fullname_ru.set()
        else:
            db.create_appeal(
                message.from_user.id, contact["phone_number"], "Consultation", 1
            )
            await state.update_data(
                {
                    "Nomer": contact["phone_number"],
                }
            )
            msg2 = f"Уважаемый {message.from_user.full_name}!\n Вы можете записаться на консультацию к психологу по проблемной ситуации, которая вас беспокоит, и получить консультацию через Zoom. Пожалуйста, подробно опишите проблемную ситуацию, по которой вы хотите получить консультацию."
            await message.answer(text=msg2, reply_markup=psychologist_page_ru)
            await appstate.app_tex_ru.set()

    else:
        await message.answer(
            "Пожалуйста, поделитесь своей контактной информацией, используя кнопку."
        )


@dp.message_handler(state=appstate.phone_ru)
async def handle_invalid_contact(message: types.Message, state: FSMContext):
    # If the user sends something other than a contact
    await message.answer(
        "Пожалуйста, поделитесь своей контактной информацией, используя кнопку."
    )
