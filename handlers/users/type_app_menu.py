from aiogram import types
from loader import dp, db, bot
from data.config import GROUP_ID
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
from keyboards.default.ApplicationPageRu import application_page_ru, phone_and_location_ru
from keyboards.default.ApplicationPageUz import application_page_uz, phone_and_location_uz
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


@dp.message_handler(text="Gaplashishni istayman", state=appstate.type_block)
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
    text="Хочу поговорить", state=appstate.type_block
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
        text == "Menga maslahat kerak"
        or text == "Мне нужна консультация"
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
        # ask user for phone or location
        if user[5] == "uz":
            await message.answer(
                "Iltimos raqamingizni yoki lokatsiyangizni yuboring.", reply_markup=phone_and_location_uz
            )
            await appstate.app_end.set()
        else:
            await message.answer(
                "Пожалуйста, отправьте свой номер телефона или местоположение.", reply_markup=phone_and_location_ru
            )
            await appstate.app_end.set()


@dp.message_handler(content_types=types.ContentType.ANY, state=appstate.app_end)
async def bot_start(message: types.Message, state: FSMContext):
    
    user_id = message.from_user.id
    user = db.select_user(id=user_id)
    
    data = await state.get_data()
    # user_id = data.get("UserID")
    modul = data.get("Modul")
    theme = data.get("Theme")
    
    msg5 = f"<b>User ID:</b> {user_id}\n<b>Modul:</b> {modul}\n<b>Murojaat turi:</b> Shoshilinch\n<b>Mavzu: </b>{theme}"
    
    if message.content_type == "contact":
        phone = message.contact.phone_number
        msg5 = f"<b>User ID:</b> {user_id}\n<b>Modul:</b> {modul}\n<b>Murojaat turi:</b> Shoshilinch\n<b>Mavzu: </b>{theme}\n<b>Telefon:</b> {phone}"
    db.create_appeal(
        user_id=user_id,
        text=theme,
        type="Anonymous",
        status=1,
        theme=theme,
    )
    
    if user[5] == "uz":
        await message.answer(
            "Murojaatingiz qabul qilindi. Tez fursatda mutaxassis javobini kuting. Zaruriyat bo'lgan taqdirda Zoom orqali maslahat olishingiz uchun havola jo'natiladi.",
            reply_markup=start,
        )
    else:
        await message.answer(
            "Ваш запрос принят. Ожидайте ответа специалиста в ближайшее время. При необходимости будет отправлена ссылка для консультации через Zoom.",
            reply_markup=start,
        )
    msg = await bot.send_message(GROUP_ID, text=msg5)
    if message.content_type == "location":
        await bot.send_location(GROUP_ID, message.location.latitude, message.location.longitude, reply_to_message_id=msg.message_id)
    await state.finish()

