from aiogram import types
from loader import dp, db
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards.default.SelectLanguage import start
from states.Appstate import appstate
from keyboards.default.PsychologistPageUz import psychologist_page_uz
from keyboards.default.PsychologistPageRu import psychologist_page_ru
from keyboards.default.Themes import (
    app_theme_ru,
    app_theme_uz,
    app_intrest_ru,
    app_intrest_uz,
)
from keyboards.default.ApplicationPageRu import application_page_ru
from keyboards.default.ApplicationPageUz import application_page_uz
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.PhoneUZ import phone_uz
from keyboards.default.PhoneRU import phone_ru


@dp.message_handler(CommandStart(), state=appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Ortga", state=appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Назад", state=appstate.type_block)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang / Выберите язык", reply_markup=start)
    await state.finish()


@dp.message_handler(text="Psixolog maslaxatiga yozilish", state=appstate.type_block)
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
    await message.answer(
        "Iltimos, tugma yordamida kontakt ma'lumotlaringizni yuboring.",
        reply_markup=phone_uz,
    )
    await appstate.phone_uz.set()


@dp.message_handler(
    text="Запишитесь на консультацию Психолога", state=appstate.type_block
)
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
    await message.answer(
        "Пожалуйста, поделитесь своей контактной информацией, используя кнопку.",
        reply_markup=phone_ru,
    )
    await appstate.phone_ru.set()


@dp.message_handler(text="Murojaat qoldirish", state=appstate.type_block)
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
    await message.answer(
        "Dastaavval seni bezovta qilayotgan mavzularidan birini tanla yoki ozin yoz:",
        reply_markup=app_theme_uz,
    )
    await appstate.app_theme.set()
    # await appstate.type_app.set()


@dp.message_handler(text="Оставить заявку", state=appstate.type_block)
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
    await message.answer(
        "Для начала, выбери одну из тем, которые тебя беспокоят или введи свою:",
        reply_markup=app_theme_ru,
    )
    await appstate.app_theme.set()
    # await appstate.type_app.set()


@dp.message_handler(state=appstate.app_theme)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    name = message.from_user.full_name
    modul = message.text
    username = message.from_user.username
    user = db.select_user(id=user_id)
    print(user)
    if username:
        user_info = f"@{username}"
    else:
        user_info = "mavjud emas"

    await state.update_data(
        {
            # "Ism": name,
            # "Nick name": user_info,
            # "UserID": user_id,
            # "Modul": modul,
            "Theme": message.text,
        }
    )
    if user[5] == "uz":
        await message.answer("Seni nima qiziqtiradi?", reply_markup=app_intrest_uz)
        await appstate.app_interest.set()
    else:
        await message.answer("Что тебя интересует?", reply_markup=app_intrest_ru)
        await appstate.app_interest.set()


@dp.message_handler(state=appstate.app_interest)
async def bot_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = db.select_user(id=user_id)
    text = message.text

    if (
        text == "Mavzuga ko'proq ma'lumot kerak"
        or text == "Хочу больше информации по теме"
    ):
        if user[5] == "uz":
            message_text = """
            Ehtimol, sen hozir xavotirdasan, yolg'izsan va umidsizsan. Sening his-tuyg'ularing sen duch kelgan vaziyat uchun normaldir. Ammo agar sen bu erda bo'lsang, yordam topishga umid qilayapsan. Bu uyat emas, balki to'g'ri qaror.
Qanday yordam berishni biladigan mutaxassislar bor, ular bu muammo bilan qanday ishlashni bilishadi. Hoziroq sen psixologdan yordam so'rashing mumkin. Sen ismingni aytmasliging mumkin. 

Seni nima bezovta qilmoqda? 

❗️ Agar biror narsa hayotingga yoki sog'lig'ingga tahdid solayotganini his qilsang, 1140 raqamiga qo'ng'iroq qil.
            """
            await message.answer(
                "Murojaat turini tanlang", reply_markup=application_page_uz
            )
            await appstate.type_app.set()
        else:
            message_text = """
            Возможно, сейчас тебе тревожно, одиноко и ты в отчаянии. Ты можешь чувствовать растерянность, гнев, бессилие. Твои чувства нормальны для той ситуации, в которой ты находишься. Но если ты здесь, значит надеешься найти помощь. Это не стыдное, а правильное решение.
Есть специалисты, которые знают, как помочь, они умеют работать с этой проблемой. Прямо сейчас ты можешь обратиться за помощью к психологу. Ты можешь также не называть своего имени.

Что тебя беспокоит? 

❗️ Если ты чувствуешь, что что-то угрожает твоей жизни или здоровью, звони 1140.
            """
            await message.answer(message_text, reply_markup=application_page_ru)
            await appstate.type_app.set()
    else:
        if user[5] == "uz":
            await message.answer(
                "Murojaat turini tanlang", reply_markup=application_page_uz
            )
            await appstate.type_app.set()
        else:
            await message.answer(
                "Выберите тип обращения.", reply_markup=application_page_ru
            )
            await appstate.type_app.set()
