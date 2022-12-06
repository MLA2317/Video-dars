from aiogram import executor
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery
from config import dp, bot
from reply import *
from Inline import *

import logging


@dp.callback_query_handler(text_contains="👍🏻")
async def like(call: CallbackQuery):
    await call.answer("Yoqdi", show_alert=True)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text_contains="👎🏻")
async def dislike(call: CallbackQuery):
    await call.answer(f"Yoqmadi", show_alert=True)
    await call.answer(cache_time=30)


@dp.callback_query_handler(text_contains="❌")
async def iks(call: CallbackQuery):
    await call.message.delete()


# start
@dp.message_handler(commands='start')
async def start(msg: Message):
    txt = f"Assalomu Aelykum {msg.from_user.full_name}! Free lesson course ga Hush kelibsiz"
    await msg.answer(txt, reply_markup=menuStart)


# help
@dp.message_handler(commands='help')
async def help(msg: Message):
    await msg.answer(f"Murajat uchun: @lazizbek_a", reply_markup=menuStart)


# menuStart
@dp.message_handler(text="Bo'limga kirish")
async def bolim(msg: Message):
    print(logging.info(msg.from_user.id))
    print(logging.info(msg.from_user.full_name))
    print(logging.info(msg.from_user.get_profile_photos))
    print(msg.from_user.values)
    await msg.answer(f"Dasturlarni tanlang!:", reply_markup=menuAsosiy)


@dp.message_handler(text="📩Biz bilan bog'lanish")
async def boglanish(msg: Message):
    txt = f"Bizga bog'lanish uchun shunga murajat qiling: @lazizbek_a" \
          f"\n" \
          f"\n" \
          f"\n" \
          f"\nTel: 99-085-23-17" \
          f"\nhttps://www.instagram.com/lazizbek__a/"
    await msg.answer(txt, reply_markup=menuStart)

# grafic
@dp.message_handler(text="🎨Grafik Dizayn")
async def grafic(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuBosh)


# Adobe Photoshop
@dp.message_handler(text="Adobe Photoshop")
async def adobep(msg: Message):
    txt = f"Adobe Photoshop"
    await msg.answer(txt, reply_markup=menuAdobe)

# back
@dp.message_handler(text="⬅Orqaga🎨")
async def adoorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBosh)

# menu Adobe Social
@dp.message_handler(text="Social design academy")
async def social(msg: Message):
    txt = f"Socially Photoshop"
    await msg.answer(txt, reply_markup=menuSocial)


# 1 dars
@dp.message_handler(text="1 - dars")
async def socbir(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/1 - Pro Photoshop 01 • kursini kutib oling.mp4", "rb")
    txt = f"Pro Photoshop darslari | 1-dars | Kirish\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await msg.answer_video(video=video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="2 - dars")
async def socikki(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/02 — Photoshop uchun qanday kompyuter kerak.mp4", "rb")
    txt = f"Pro Photoshop darslari | 2-dars | Photoshop uchun qanday kompyuter kerak\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="3 - dars")
async def socuch(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/03 — Photoshop’ni o‘rnatish.mp4", "rb")
    txt = f"Pro Photoshop darslari | 3-dars |  Photoshop’ni o‘rnatish\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="4 - dars")
async def soctort(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/04 — Foydalanuvchi interfeysi.mp4", "rb")
    txt = f"Pro Photoshop darslari | 4-dars | Foydalanuvchi interfeysi\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="5 - dars")
async def socbesh(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/05 — Foydalanuvchi interfeysi.mp4", "rb")
    txt = f"Pro Photoshop darslari | 5-dars | Foydalanuvchi interfeysi\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="6 - dars")
async def socolti(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/06 — Photoshop'da navigatsiya.mp4", "rb")
    txt = f"Pro Photoshop darslari | 6-dars | Photoshop'da navigatsiya\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="7 - dars")
async def socyetti(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/07 — Suratlar bilan ishlash.mp4", "rb")
    txt = f"Pro Photoshop darslari | 7-dars | Suratlar bilan ishlash\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="8 - dars")
async def socsakkiz(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/08 — Surat hajmi va o'lchami.mp4", "rb")
    txt = f"Pro Photoshop darslari | 8-dars | Surat hajmi va o'lcham\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="9 - dars")
async def soctoqqiz(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/09 — Photoshop’da suratlarni qirqish.mp4", "rb")
    txt = f"Pro Photoshop darslari | 9-dars | Photoshop’da suratlarni qirqish\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="10 - dars")
async def socon(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Social design academy/10 — Ranglar palitrasi.mp4", "rb")
    txt = f"Pro Photoshop darslari | 10-dars | Ranglar palitrasi\n \nYoutube — www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga⬅")
async def socorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuAdobe)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def socasosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuIthouse
@dp.message_handler(text="IT hause Design")
async def house(msg: Message):
    txt = f"IT design phtoshop"
    await msg.answer(txt, reply_markup=menuIThouse)


# 1 dars
@dp.message_handler(text="1-dars")
async def itbir(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-o-rnatish-1-dars.mp4", "rb")
    txt = f"Photoshop darslari | 1-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_edu" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="2-dars")
async def itikki(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-2-dars.mp4", "rb")
    txt = f"Photoshop darslari | 2-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="3-dars")
async def ituch(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik_Dizayn_Photoshop_3_dars_xd03jeXYn6k_134.mp4", "rb")
    txt = f"Photoshop darslari | 3-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="4-dars")
async def ittort(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-4-dars.mp4", "rb")
    txt = f"Photoshop darslari | 4-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="5-dars")
async def itbesh(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-5-dars.mp4", "rb")
    txt = f"Photoshop darslari | 5-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="6-dars")
async def itolti(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-6-dars.mp4", "rb")
    txt = f"Photoshop darslari | 6-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="7-dars")
async def ityetti(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik-Dizayn-Photoshop-7-dars.mp4", "rb")
    txt = f"Photoshop darslari | 7-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram —  https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="8-dars")
async def itsakkiz(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik_Dizayn_Photoshop_8_dars_L1HufZTIOmY_136.mp4", "rb")
    txt = f"Photoshop darslari | 8-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="9-dars")
async def ittoqqiz(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik_Dizayn_Photoshop_9_dars_QPIgcWsZw88_136.mp4", "rb")
    txt = f"Photoshop darslari | 9-dars | Kirish\n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="10-dars")
async def iton(msg: Message):
    video = open("video/grafik/Adobe Photoshop/Photoshop/Grafik_Dizayn_Photoshop_10_dars_j2Q_BsuGbLY_136.mp4", "rb")
    txt = f"Photoshop darslari | 10-dars | \n \nYoutube — www.youtube.com/channel/UCYc_P1e4JUSFi_2hiY_eCIw\nTelegram — https://t.me/ithouse_ed" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga⬅")
async def itorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuAdobe)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# back
@dp.message_handler(text="⬅Ortga🎨")
async def boshorqaga(msg: Message):
    await msg.answer(f"⬅Ortga", reply_markup=menuBosh)


# Adobe Illistrate
@dp.message_handler(text="Adobe Illistrate")
async def illistra(msg: Message):
    txt = f"Adobe Illistarte"
    await msg.answer(txt, reply_markup=menuIllistrate)


# 1 dars
@dp.message_handler(text="1 -dars")
async def illbir(msg: Message):
    video = open("video/grafik/Adobe illistate/#1 Adobe Illustrator Kirish.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 1-dars |  Kirish\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="2 -dars")
async def illikki(msg: Message):
    video = open("video/grafik/Adobe illistate/#2 Adobe Illustrator Yangi fayl yaratish.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 2 -dars |  Yangi fayl yaratish\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="3 -dars")
async def illuch(msg: Message):
    video = open("video/grafik/Adobe illistate/#3 Adobe Illustrator Yangi workspace yaratish.mp4", "rb")
    txt = f"Adobe Illustrator darslari| 3-dars | Yangi workspace yaratish\n \nYoutube — Youtube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="4 -dars")
async def illtort(msg: Message):
    video = open("video/grafik/Adobe illistate/#4 Ish maydoni va artboard.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 4 -dars | Ish maydoni va artboard\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="5 -dars")
async def illbesh(msg: Message):
    video = open("video/grafik/Adobe illistate/#5 Golden Ratio nima.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 5 -dars |  Golden Ratio nima\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="6 -dars")
async def illolti(msg: Message):
    video = open("video/grafik/Adobe illistate/#6 Twitter logosi.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 6 -dars |  Twitter logosi\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="7 -dars")
async def illyetti(msg: Message):
    video = open("video/grafik/Adobe illistate/#7 Illustrator  Pathfinder imkoniyatlari.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 7 -dars |  Pathfinder imkoniyatlari\n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="8 -dars")
async def illsakkiz(msg: Message):
    video = open("video/grafik/Adobe illistate/#8 Fayllarni saqlash va export qilish.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 8 -dars |  Fayllarni saqlash va export \n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="9 -dars")
async def illtoqqiz(msg: Message):
    video = open("video/grafik/Adobe illistate/#9 Adobe Illustratorda 5ta foydali sozlamalar.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 9 -dars |  Adobe Illustratorda 5ta  \n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="10 -dars")
async def illon(msg: Message):
    video = open("video/grafik/Adobe illistate/#10 Pen Tool bilan ishlash.mp4", "rb")
    txt = f"Adobe Illustrator darslari | 10 -dars |  Pen Tool bilan ishlash  \n \nYoutube — http://www.youtube.com/c/MadinaMavlonova\nTelegram — @illustros" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga⬅")
async def illorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBosh)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# AdobeXd
@dp.message_handler(text="Adobe XD")
async def adobexd(msg: Message):
    txt = f"Adobe XD"
    await msg.answer(txt, reply_markup=menuAdobeXd)


# 1 dars
@dp.message_handler(text="1- dars")
async def xdbir(msg: Message):
    video = open("video/grafik/Adobe XD/01 Dasturni ko‘chirib olish.mp4", "rb")
    txt = f"Adobe XD | 1-dars | Dasturni ko‘chirib olish\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="2- dars")
async def xdikki(msg: Message):
    video = open("video/grafik/Adobe XD/02 Dasturning kirish oynasi.mp4", "rb")
    txt = f"Adobe XD | 2-dars |  Dasturning kirish oynasi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="3- dars")
async def xduch(msg: Message):
    video = open("video/grafik/Adobe XD/03 Artboard tuzish.mp4", "rb")
    txt = f"Adobe XD | 3-dars | Artboard tuzish\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="4- dars")
async def cdtort(msg: Message):
    video = open("video/grafik/Adobe XD/04 Rectangle asbobi.mp4", "rb")
    txt = f"Adobe XD | 4-dars |  Rectangle asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="5- dars")
async def xdbesh(msg: Message):
    video = open("video/grafik/Adobe XD/05 Ellipse asbobi.mp4", "rb")
    txt = f"Adobe XD | 5-dars | Ellipse asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="6- dars")
async def xdolti(msg: Message):
    video = open("video/grafik/Adobe XD/06 Polygon asbobi.mp4", "rb")
    txt = f"Adobe XD | 6-dars | Polygon asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="7- dars")
async def xdyetti(msg: Message):
    video = open("video/grafik/Adobe XD/07 Line asbobi.mp4", "rb")
    txt = f"Adobe XD | 7-dars | Line asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="8- dars")
async def xdsakkiz(msg: Message):
    video = open("video/grafik/Adobe XD/08 Pen asbobi (1).mp4", "rb")
    txt = f"Adobe XD | 8-dars | Pen asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="9- dars")
async def xdtoqqiz(msg: Message):
    video = open("video/grafik/Adobe XD/09 Pen asbobi (2).mp4", "rb")
    txt = f"Adobe XD | 9-dars | Pen asbobi (2)\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="10- dars")
async def xdon(msg: Message):
    video = open("video/grafik/Adobe XD/10 Text asbobi.mp4", "rb")
    txt = f"Adobe XD | 10-dars | Text asbobi\n \nYoutube — http://www.youtube.com/c/Sociallyuz\nTelegram — @sociallyuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Ortga⬅")
async def xdorqaga(msg: Message):
    await msg.answer(f"⬅Orgga", reply_markup=menuBosh)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# program
@dp.message_handler(text="💻Program kurslar")
async def program(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuIT)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

# menuFronBAck
@dp.message_handler(text="Front-end/Back-end")
async def frontback(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuFronBack)


# back
@dp.message_handler(text="⬅Orqaga 💻")
async def frontbacqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuIT)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuFront
@dp.message_handler(text="Front-End")
async def front(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuFront)


# back
@dp.message_handler(text="⬅Orqaga🔙")
async def fronqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFronBack)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# HTML
@dp.message_handler(text="HTML")
async def boost(msg: Message):
    txt = f"HTML!"
    await msg.answer(txt, reply_markup=menuHTML)


# 1 dars
@dp.message_handler(text="HTML 1 - dars")
async def htmlbir(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/01-HTML Asosiy tushunchalar.mp4", "rb")
    txt = f"HTML | 1-dars |  Asosiy tushunchalar\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="HTML 2 - dars")
async def htmlikki(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/02-HTML - Tuzulmasi.mp4", "rb")
    txt = f"HTML | 2-dars | Tuzilmasi\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="HTML 3 - dars")
async def htmluch(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/03-HTML - head, body haqida.mp4", "rb")
    txt = f"HTML | 3-dars | Head, body haqida\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="HTML 4 - dars")
async def htmltort(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/04-HTML - dasturlashni boshladek.mp4", "rb")
    txt = f"HTML | 4-dars | Dasturlashni boshladik\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="HTML 5 - dars")
async def htmlbesh(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/05-HTML - taglar haqida ko'piroq.mp4", "rb")
    txt = f"HTML | 5-dars | Taglar haqida\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="HTML 6 - dars")
async def htmlolti(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/06-HTML- li teglari haqida.mp4", "rb")
    txt = f"HTML | 6-dars | li teglari haqida\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="HTML 7 - dars")
async def htmlyetti(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/07-HTML-form.mp4", "rb")
    txt = f"HTML | 7-dars |  Formlar haqida\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="HTML 8 - dars")
async def htmlsakkiz(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/08-HTML- Foydali ma'lumotlar.mp4", "rb")
    txt = f"HTML | 8-dars |  Foydali ma'lumotlar\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="HTML 9 - dars")
async def htmltoqiz(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/09-HTML- Form workshop.mp4", "rb")
    txt = f"HTML | 9-dars | Form workshop\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="HTML 10 - dars")
async def htmlon(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/HTML/10-HTML- Media elementlari.mp4", "rb")
    txt = f"HTML | 10-dars | Media elementlari\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 11dars
@dp.message_handler(text="HTML 11 - dars")
async def htmlonbir(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/HTML/HTML_AJOYIB_XUSUSIYAT_HTMLDA_RASM_XARITA_TUZISH_HTML_IMG_MAP.mp4",
        "rb")
    txt = f"HTML | 11-dars | HTML da rasm xarita tuzish\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🔴")
async def htmlorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFront)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# css
@dp.message_handler(text="CSS")
async def css(msg: Message):
    txt = f"CSS!"
    await msg.answer(txt, reply_markup=menuCSS)


# 1 dars
@dp.message_handler(text="CSS 1 - dars")
async def cssbir(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#01- CSS Asoslari.mp4", "rb")
    txt = f"CSS | 1-dars | CSS Asoslari\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="CSS 2 - dars")
async def cssikki(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#02 - CSS Fonlar.mp4", "rb")
    txt = f"CSS | 2-dars | CSS Fonla\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="CSS 3 - dars")
async def cssuch(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#03 - CSS Border.mp4", "rb")
    txt = f"CSS | 3-dars |  CSS Border\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="CSS 4 - dars")
async def csstort(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#04 - CSS Margin , Padding, Width, Height.mp4", "rb")
    txt = f"CSS | 4-dars | CSS Margin , Padding, Width, Height\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="CSS 5 - dars")
async def cssbesh(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#05 - CSS Font.mp4", "rb")
    txt = f"CSS | 5-dars | CSS Font\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="CSS 6 - dars")
async def cssolti(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#06 - css uzbek - dispaly.mp4", "rb")
    txt = f"CSS | 6-dars | Display\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="CSS 7 - dars")
async def cssyetti(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#7 css uzbek - position haqida.mp4", "rb")
    txt = f"CSS | 7-dars | Position haqida\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="CSS 8 - dars")
async def csssakkiz(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#08 - CSS Table.mp4", "rb")
    txt = f"CSS | 8-dars | Table\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="CSS 9 - dars")
async def csstoqqiz(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#09 - CSS Float & Layout.mp4", "rb")
    txt = f"CSS | 9-dars | Float & Layout\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="CSS 10 - dars")
async def csson(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/CSS/#10 - CSS Float workshop.mp4", "rb")
    txt = f"CSS | 10-dars |  Float workshop\n \nYoutube — http://www.youtube.com/c/Alitechacademy\nTelegram — @alitechuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🔵")
async def cssorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFront)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# javascript
@dp.message_handler(text="JavaScript")
async def javascript(msg: Message):
    txt = f"JavaScripts!"
    await msg.answer(txt, reply_markup=menuJavascript)


# 1 dars
@dp.message_handler(text="JavaScrip 1 - dars")
async def javascribbir(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/1-dars. JavaScript darslari __ O'zgaruvchilar.mp4", "rb")
    txt = f"JavaScripts | 1-dars | O'zgaruvchilar\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="JavaScrip 2 - dars")
async def javascribikki(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/2-dars. JavaScript darslari __ Primitive turlar.mp4",
        "rb")
    txt = f"JavaScripts | 2-dars | Primitive turlar\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="JavaScrip 3 - dars")
async def javascribuch(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/JavaScripts/3-dars. JavaScript darslari __ Object.mp4",
                 "rb")
    txt = f"JavaScripts | 3-dars | Object\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="JavaScrip 4 - dars")
async def javascribtort(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/JavaScripts/4-dars. JavaScript darslari __ Array.mp4", "rb")
    txt = f"JavaScripts | 4-dars | Array\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="JavaScrip 5 - dars")
async def javascribbesh(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/JavaScripts/5-dars. JavaScript darslari __ Function.mp4",
                 "rb")
    txt = f"JavaScripts | 5-dars | Function\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="JavaScrip 6 - dars")
async def javascribolti(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/6-dars. JavaScript darslari __ Arifmetik operatorlar.mp4",
        "rb")
    txt = f"JavaScripts | 6-dars | Arifmetik operatorlar\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="JavaScrip 7 - dars")
async def javascribyetti(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/7_dars_JavaScript_darslari_Solishtiruv_va_tenglik_operatorlari.mp4",
        "rb")
    txt = f"JavaScripts | 7-dars | Solishtiruv va tenglik operatorlari\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="JavaScrip 8 - dars")
async def javascribsakkiz(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/8-dars. JavaScript darslari __ Ternary operatori.mp4",
        "rb")
    txt = f"JavaScripts | 8-dars | Ternary operatori\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="JavaScrip 9 - dars")
async def javascribtoqqiz(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Front-end/JavaScripts/9_dars_JavaScript_darslari_Boolean_algebra,_mantiqiy_hamda_bitwise.mp4",
        "rb")
    txt = f"JavaScripts | 9-dars | TBoolean algebra, mantiqiy hamda bitwise operatorlari\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="JavaScrip 10 - dars")
async def javascribon(msg: Message):
    video = open("video/Program/Front-end Backend/Front-end/JavaScripts/10-dars. JavaScript darslari __ If else.mp4",
                 "rb")
    txt = f"JavaScripts | 10-dars | If else\n \nYoutube — http://www.youtube.com/c/UsmonMasudjonov\nTelegram — @usmon_masudjonov" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🟡")
async def javascriptorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFront)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuBackend
@dp.message_handler(text="Back-End")
async def backend(msg: Message):
    txt = f"Quyidigilarni Tanlang!"
    await msg.answer(txt, reply_markup=menuBackend)


# back
@dp.message_handler(text="⬅Orqaga🔷")
async def frontbackorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFronBack)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuPython
@dp.message_handler(text="Python")
async def python(msg: Message):
    txt = f"Python"
    await msg.answer(txt, reply_markup=menuPython)


# 1dars
@dp.message_handler(text="Python 1 - dars")
async def pythonbir(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#00 Python Darslari _ Kirish so'z.mp4", "rb")
    txt = f"Python | 1-dars | Kirish\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="Python 2 - dars")
async def pythonikki(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#00 Python Darslari _ mohirdev.uz bilan tanishuv.mp4",
                 "rb")
    txt = f"Python | 2-dars | mohirdev.uz bilan tanishuv\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="Python 3 - dars")
async def pythonuch(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#01 Python Darslari _ Anaconda o'rnatamiz.mp4", "rb")
    txt = f"Python | 3-dars | Anaconda o'rnatamiz\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="Python 4 - dars")
async def pythontort(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Python/#01 Python Darslari _ Brauzerda kod yozish (Repl.it).mp4",
        "rb")
    txt = f"Python | 4-dars | Brauzerga kod yozish\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="Python 5 - dars")
async def pythonbesh(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#02 Python Darslari _ Birinchi Dasturimiz.mp4", "rb")
    txt = f"Python | 5-dars | Birinchi Dasturimiz\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="Python 6 - dars")
async def pythonolti(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Python/#03 Python Darslari _ print(), Arifmetik amallar va Sinteks.mp4",
        "rb")
    txt = f"Python | 6-dars | print(), Arifmetik amallar va Sinteks\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="Python 7 - dars")
async def pythonyetti(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#04 Python Darslari _ O'zgaruvchilar (Variables).mp4",
                 "rb")
    txt = f"Python | 7-dars | O'zgaruvchilar (Variables)\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="Python 8 - dars")
async def pythonsakkiz(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Python/#05 Python Darslari _ Matn bilan ishlash (Strings).mp4", "rb")
    txt = f"Python | 8-dars | Matn bilan ishlash (Strings)\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="Python 9 - dars")
async def pythontoqqiz(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#06 Python Darslari _ Sonlar bilan ishlash.mp4", "rb")
    txt = f"Python | 9-dars | Sonlar bilan ishlash\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="Python 10 - dars")
async def pythonon(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Python/#07 Python Darslari _ Lists (Ro'yxatlar).mp4", "rb")
    txt = f"Python | 10-dars | Lists (Ro'yxatlar)\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 11dars
@dp.message_handler(text="Python 11 - dars")
async def pythononbir(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Python/#08_Python_Darslari_Ro'yxat_bilan_ishlash_O'zgarmas_ro'yxatlar_Tuples.mp4",
        "rb")
    txt = f"Python | 11-dars | Ro'yhat bilan ishlash. O'zgarmas royxatlar(Tuples)\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 12dars
@dp.message_handler(text="Python 12 - dars")
async def pythononikki(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Python/#09 Python Darslari _ for tsikli bilan tanishamiz.mp4", "rb")
    txt = f"Python | 12-dars | for tsikl bilan tanishamiz\n \nYoutube — http://www.youtube.com/c/Sariqdev\nTelegram — @sariqdev" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🔹")
async def pythonorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBackend)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuJava
@dp.message_handler(text="Java")
async def java(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuJava)


# 1dars
@dp.message_handler(text="Java 1 - dars")
async def javabir(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Java/Java_for_Beginners_Uzbek_1_Istalling_the_JDK,Downloading_Eclipse.mp4",
        "rb")
    txt = f" Java| 1-dars | Kirish\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="Java 2 - dars")
async def javaikki(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -2- Variables.mp4", "rb")
    txt = f" Java| 2-dars | Variables\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3dars
@dp.message_handler(text="Java 3 - dars")
async def javauch(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -3- Promotion and Casting.mp4", "rb")
    txt = f" Java| 3-dars | Promotion and Casting\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="Java 4 - dars")
async def javatort(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Java/Java_for_Beginners_Uzbek_4_Wrapper_Class_and_Initialization.mp4",
        "rb")
    txt = f" Java| 4-dars | Wrapper Class and Initialization\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="Java 5 - dars")
async def javabesh(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Java/Java_for_Beginners_Uzbek_5_System_Class_and_Console_Print.mp4",
        "rb")
    txt = f" Java| 5-dars | Class and Console Print\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6dars
@dp.message_handler(text="Java 6 - dars")
async def javaolti(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -6- Keyboard Input.mp4",
                 "rb")
    txt = f" Java| 6-dars | Keyboard Input\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7dars
@dp.message_handler(text="Java 7 - dars")
async def javayetti(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -7- If Statement.mp4", "rb")
    txt = f" Java| 7-dars | If Statement\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8dars
@dp.message_handler(text="Java 8 - dars")
async def javasakkiz(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -10- while, do_while.mp4",
                 "rb")
    txt = f" Java| 8-dars | While, Do while\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9dars
@dp.message_handler(text="Java 9 - dars")
async def javatoqqiz(msg: Message):
    video = open(
        "video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -9- for _break,continue,label.mp4",
        "rb")
    txt = f" Java| 9-dars | For break,continue\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10dars
@dp.message_handler(text="Java 10 - dars")
async def javaon(msg: Message):
    video = open("video/Program/Front-end Backend/Back-end/Java/Java for Beginners [Uzbek] -11- Methods.mp4", "rb")
    txt = f" Java| 10-dars | Method\n \nYoutube — http://www.youtube.com/channel/UCFMPyPzKbQ4YxhBbc4x1hhw/playlists" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🔸")
async def javaorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBackend)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


# menuadnroid\ios
@dp.message_handler(text="Android/IOS")
async def androidios(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuAndroidIOS)

# back
@dp.message_handler(text="⬅Orqaga🔻")
async def androidiosqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuIT)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#IOS
@dp.message_handler(text="IOS")
async def ios(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuIOS)

# 1dars
@dp.message_handler(text="IOS 1 - dars")
async def iosbir(msg: Message):
    video = open(
        "video/Program/Android ios/IOS/Swift for Beginners Part 1_ Getting Started.mp4",
        "rb")
    txt = f" IOS| 1-dars | Getting Started\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="IOS 2 - dars")
async def iosikki(msg: Message):
    video = open(
        "video/Program/Android ios/IOS/Swift for Beginners Part 2_ Variables & Constants.mp4",
        "rb")
    txt = f" IOS| 2-dars | Variables & Constants\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3dars
@dp.message_handler(text="IOS 3 - dars")
async def iosuch(msg: Message):
    video = open(
        "video/Program/Android ios/IOS/Swift for Beginners Part 3 - Types.mp4",
        "rb")
    txt = f" IOS| 3-dars | Types\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4dars
@dp.message_handler(text="IOS 4 - dars")
async def iostort(msg: Message):
    video = open(
        "video/Program/Android ios/IOS/Swift for Beginners Part 4 - Functions & Parameters.mp4",
        "rb")
    txt = f" IOS| 4-dars | Functions & Parameters\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="IOS 5 - dars")
async def iosbesh(msg: Message):
    video = open(
        "video/Program/Android ios/IOS/Swift for Beginners Part 5 - Classes & Structs.mp4",
        "rb")
    txt = f" IOS| 5-dars | Classes & Structs\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga🔺")
async def iosorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuAndroidIOS)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Android
@dp.message_handler(text="Android")
async def android(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuFlutterkotlin)

#Flutter
@dp.message_handler(text="Flutter")
async def flutter(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuFlutter)


# 1dars
@dp.message_handler(text="Flutter 1 - dars")
async def Flutterbir(msg: Message):
    video = open(
        "video/Program/Android ios/Android/flutter/01 - Flutter SDKni o'rnatish _ Flutterni sozlash.mp4",
        "rb")
    txt = f" Flutter| 1-dars |  Flutter SDKni o'rnatish, Flutterni sozlash\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="Flutter 2 - dars")
async def Flutterikki(msg: Message):
    video = open(
        "video/Program/Android ios/Android/flutter/02 - Flutter tanishuv _ Hello World.mp4",
        "rb")
    txt = f" Flutter| 2-dars |  Flutter tanishuv\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3dars
@dp.message_handler(text="Flutter 3 - dars")
async def Flutteruch(msg: Message):
    video = open(
        "video/Program/Android ios/Android/flutter/03_Flutter_Scaffold_widget_Image_widget'lari_bilan_tanishamiz.mp4",
        "rb")
    txt = f" Flutter| 3-dars |  Flutter Scaffold widget\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 4dars
@dp.message_handler(text="Flutter 4 - dars")
async def Fluttertort(msg: Message):
    video = open(
        "video/Program/Android ios/Android/flutter/04 - Flutter AssetImage widget _ pubspec.yaml.mp4",
        "rb")
    txt = f" Flutter| 4-dars | Flutter AssetImage widget\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="Flutter 5 - dars")
async def Flutterbesh(msg: Message):
    video = open(
        "video/Program/Android ios/Android/flutter/05 - Flutter App icon'ni o'zgartirish va sozlash.mp4",
        "rb")
    txt = f" Flutter| 5-dars | Flutter App icon'ni o'zgartirish va sozlash\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga▪")
async def flutterorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFlutterkotlin)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#Kotlin
@dp.message_handler(text="Kotlin")
async def kotlin(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuKotlin)


# 1dars
@dp.message_handler(text="Kotlin 1 - dars")
async def Kotlinbir(msg: Message):
    video = open(
        "video/Program/Android ios/Android/kotlin/1 - RecyclerView Custom Basic Adapter(Kotlin).mp4",
        "rb")
    txt = f" Kotlin darslari| 1-dars | RecyclerView Custom Basic Adapter(Kotlin)\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="Kotlin 2 - dars")
async def Kotlinikki(msg: Message):
    video = open(
        "video/Program/Android ios/Android/kotlin/2 - RecyclerView Custom Multitype Adapter(Kotlin).mp4",
        "rb")
    txt = f" Kotlin darslari| 2-dars | RecyclerView Custom Multitype Adapter(Kotlin)\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3dars
@dp.message_handler(text="Kotlin 3 - dars")
async def Kotlinuch(msg: Message):
    video = open(
        "video/Program/Android ios/Android/kotlin/3_RecyclerView_Custom_Adapter_with_Header_and_FooterKotlin.mp4",
        "rb")
    txt = f" Kotlin darslari| 3-dars |  RecyclerView Custom Adapter with Header and Footer(Kotlin)\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 4dars
@dp.message_handler(text="Kotlin 4 - dars")
async def Kotlintort(msg: Message):
    video = open(
        "video/Program/Android ios/Android/kotlin/4 - RecyclerView Custom Adapter Loading More(Kotlin).mp4",
        "rb")
    txt = f" Kotlin darslari| 4-dars |  RecyclerView Custom Adapter Loading More(Kotlin)\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 5dars
@dp.message_handler(text="Kotlin 5 - dars")
async def Kotlinbesh(msg: Message):
    video = open(
        "video/Program/Android ios/Android/kotlin/5 - RecyclerView inside RecyclerView(Kotlin).mp4",
        "rb")
    txt = f" Kotlin darslari| 5-dars | RecyclerView inside RecyclerView(Kotlin)\n \nYoutube — http://www.youtube.com/c/iOSAcademy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga▫")
async def kotlinorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuFlutterkotlin)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



# back
@dp.message_handler(text="⬅Orqaga🔳")
async def androidiosorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuAndroidIOS)


# menusql\mysql
@dp.message_handler(text="PostreSQL/MySQL")
async def postremysql(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuSQLMySQL)


# back
@dp.message_handler(text="⬅Orqaga ©")
async def mysqlpostorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuIT)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#postgresql
@dp.message_handler(text="PostgreSQL")
async def postgresql(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuPostgreSQL)

# 1dars
@dp.message_handler(text="PostgreSQL 1 - dars")
async def postgresqlbbir(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/PostgreSQL/PostgreSQL 1-dars. Kompyuterimizga Postgresni o'rnatamiz.mp4",
        "rb")
    txt = f" PostgreSQL| 1-dars | Kompyuterimizga Postgresni o'rnatamiz\n \nYoutube — http://www.youtube.com/c/BexruzXolmuminov \nTelegram - @bexruz_ru" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="PostgreSQL 2 - dars")
async def postgresqlbikki(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/PostgreSQL/PostgreSQL_2_dars_Database_yaratish,_unga_ulanish_va_o'chirish.mp4",
        "rb")
    txt = f" PostgreSQL| 2-dars | Database yaratish, unga ulanish va o'chirish\n \nYoutube — http://www.youtube.com/c/BexruzXolmuminov \nTelegram - @bexruz_ru" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3dars
@dp.message_handler(text="PostgreSQL 3 - dars")
async def postgresqluch(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/PostgreSQL/PostgreSQL_3_dars_Table_yaratish,_uni_o'chirish_va_Data_Typle_lar.mp4",
        "rb")
    txt = f" PostgreSQL| 3-dars | Table yaratish, uni o'chirish va DataTyple lar haqida\n \nYoutube — http://www.youtube.com/c/BexruzXolmuminov \nTelegram - @bexruz_ru" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 4dars
@dp.message_handler(text="PostgreSQL 4 - dars")
async def postgresqltort(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/PostgreSQL/PostgreSQL_4_dars_Jadvalga_ma'lumot_yozish_INSERT_INTO.mp4",
        "rb")
    txt = f" PostgreSQL| 4-dars | Jadvalga ma'lumot yozish. (INSERT INTO)\n \nYoutube — http://www.youtube.com/c/BexruzXolmuminov \nTelegram - @bexruz_ru" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="PostgreSQL 5 - dars")
async def postgresqlbesh(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/PostgreSQL/PostgreSQL_5_dars_Mokaroo_sayti_orqali_default_datalar_yaratish.mp4",
        "rb")
    txt = f" PostgreSQL| 5-dars |Mokaroo sayti orqali default datalar yaratish\n \nYoutube — http://www.youtube.com/c/BexruzXolmuminov \nTelegram - @bexruz_ru" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga©")
async def iosorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuSQLMySQL)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#mysql
@dp.message_handler(text="MySQL")
async def mysql(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuMySQL)


# 1dars
@dp.message_handler(text="MySQL 1 - dars")
async def mysqlbir(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/MySQL/MySQL #1-Dars. Kirish.mp4",
        "rb")
    txt = f" MySQL| 1-dars | Kirish\n \n Youtube — http://www.youtube.com/c/CodeLeader \nTelegram - @codeleaderuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2dars
@dp.message_handler(text="MySQL 2 - dars")
async def mysqlikki(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/MySQL/MySQL #2-Dars.Jadval yaratish - Create Table.mp4",
        "rb")
    txt = f" MySQL| 2-dars | Jadval yaratish - Create Table\n \n Youtube — http://www.youtube.com/c/CodeLeader \nTelegram - @codeleaderuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3dars
@dp.message_handler(text="MySQL 3 - dars")
async def mysqluch(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/MySQL/MySQL #3-Dars. Insert, Update, Delete.mp4",
        "rb")
    txt = f" MySQL| 3-dars | Insert, Update, Delete\n \n Youtube — http://www.youtube.com/c/CodeLeader \nTelegram - @codeleaderuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 4dars
@dp.message_handler(text="MySQL 4 - dars")
async def mysqltort(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/MySQL/MySQL #4-Dars. Select, count, sum, order by.mp4",
        "rb")
    txt = f" MySQL| 4-dars | Select, count, sum, order by\n \n Youtube — http://www.youtube.com/c/CodeLeader \nTelegram - @codeleaderuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5dars
@dp.message_handler(text="MySQL 5 - dars")
async def mysqlbesh(msg: Message):
    video = open(
        "video/Program/Malumot bazasi/MySQL/MySQL #5 – Dars. Alter Table.mp4",
        "rb")
    txt = f" MySQL| 5-dars |Alter Table\n \n Youtube — http://www.youtube.com/c/CodeLeader \nTelegram - @codeleaderuz" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# back
@dp.message_handler(text="⬅Orqaga®")
async def flutterorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuSQLMySQL)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)




#menuKompyutersavodxonligi
@dp.message_handler(text="🖥Kompyuter Savodxonligi")
async def kompyutersavod(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuKompyutersavod)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#kompyuter0dan
@dp.message_handler(text="Kampyuter 0 dan organish")
async def kompyuterorganish(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuKampyuter0dan)

# 1- dars
@dp.message_handler(text="kompyuter organish 1 dars")
async def komorganishbir(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterni o'rganish 1-dars 2020.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 1-dars \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 2- dars
@dp.message_handler(text="kompyuter organish 2 dars")
async def komorganishikki(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterni o'rganish 2-dars 2020.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 2-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="kompyuter organish 3 dars")
async def komorganishuch(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterni o'rganish 3-dars 2020.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 3-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="kompyuter organish 4 dars")
async def komorganishtort(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterni o'rganish 4-Dars.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 4-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="kompyuter organish 5 dars")
async def komorganishbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterni O'rganish 5-dars.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 5-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 6- dars
@dp.message_handler(text="kompyuter organish 6 dars")
async def komorganisholti(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Kompyuterda Fayllarni yashirish@6-Dars.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 6-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7- dars
@dp.message_handler(text="kompyuter organish 7 dars")
async def komorganishyetti(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Minyu Puskni Nastroyka Qilish@7-Dars.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 7-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8- dars
@dp.message_handler(text="kompyuter organish 8 dars")
async def komorganishbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/КОМПЬЮТЕРНИ УРГАНИШ 8-ДАРС.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 8-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 9- dars
@dp.message_handler(text="kompyuter organish 9 dars")
async def komorganishbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/Ноутбук_Сенсор_Сичкончасини_Ёкиш_Ва_Учириш_2020.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 9-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 10- dars
@dp.message_handler(text="kompyuter organish 10 dars")
async def komorganishbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Kompyuter 0 dan organish/КОМЬПЮТЕРНИ УРГАНИШ 10-ДАРС.mp4",
        "rb")
    txt = f" |Kompyuterni o'rganish 10-dars 2020 \n \n Youtube — http://bit.ly/3sZVumK" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# back
@dp.message_handler(text="⬅Orqaga🖥")
async def komporgaorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuKompyutersavod)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#menuwindowsornatish
@dp.message_handler(text="Windows ornatish")
async def windsornatish(msg: Message):
    await msg.answer(f"Quyidagilarni tanlang!", reply_markup=menuWindows)

#1 - dars
@dp.message_handler(text="Windows 1 - dars")
async def windowsbir(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Windows_10_yangilanishi,_dasturlarini_va_ayg'oqchi_funksiyalarini.mp4",
        "rb")
    txt = f" |📹 1. Windows 10 yangilanishi, dasturlarini va ayg'oqchi funksiyalarini o'chirish\n \n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 2- dars
@dp.message_handler(text="Windows 2 - dars")
async def windowsikki(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Windows (788.110) ni aktivatsiya qilish (faollashtirish).mp4",
        "rb")
    txt = f" |📹 2.Windows (7/8/8.1/10) ni aktivatsiya qilish (faollashtirish) \n \n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Windows 3 - dars")
async def windowsuch(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Windows'larning_barcha_turlari,_redaksiyalari_Pro,_LTSB_va_b_bilan.mp4",
        "rb")
    txt = f" |📹 3. Windows'larning barcha turlari, redaksiyalari (Pro, LTSB va b.) bilan tanishamiz! Windows tanlaymiz! \n" \
          f" \n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4- dars
@dp.message_handler(text="Windows 4 - dars")
async def windowstort(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Istalgan_Windows_788_110_ni_yuklash_va_fleshkaga_yozishni_2_usuli!.mp4",
        "rb")
    txt = f" |📹 4. Istalgan Windows (7/8/8.1/10) ni yuklash va fleshkaga yozishni 2 usuli! \n" \
          f" \n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Windows 5 - dars")
async def windowsbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Windows 10 o'rnatish.mp4",
        "rb")
    txt = f" |📹 5. Windows 10 o'rnatish \n \n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6- dars
@dp.message_handler(text="Windows 6 - dars")
async def windowsolti(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Drayverlarni_onlayn_va_oflayn_yangilash_DriverPack_dasturlari_bilan.mp4",
        "rb")
    txt = f" |📹 6. Drayverlarni onlayn va oflayn yangilash. DriverPack dasturlari bilan ishlash. \n " \
          f"\n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 7- dars
@dp.message_handler(text="Windows 7 - dars")
async def windowsyetti(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Dasturlarni avtomatik o'rnatuvchi dasturlar.mp4",
        "rb")
    txt = f" |📹 7. Dasturlarni avtomatik o'rnatuvchi dasturlar \n " \
          f"\n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 8- dars
@dp.message_handler(text="Windows 8 - dars")
async def windowssakiz(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows ornatish/Original_Windows'ni_yuklashni_o'rganamiz!_Nega_faqat_original_Windows.mp4",
        "rb")
    txt = f" |📹 8. Original Windows'ni yuklashni o'rganamiz! Nega faqat original Windows faylidan foydalanish kerak? \n " \
          f"\n Telegram - @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# back
@dp.message_handler(text="⬅Orqaga 🖥")
async def komporgaorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuKompyutersavod)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)




#windows zaruriy sozlamalr
@dp.message_handler(text="Windows zaruriy sozlamalar")
async def windowszaruriysoz(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuWindowszaruriy)

# 1- dars
@dp.message_handler(text="Windows zaruriy 1 - dars")
async def windowszarbir(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Kompyuter_yonish_payti_parol_so'ramaydigan_qilib_sozlash_Kompyuterga.mp4",
        "rb")
    txt = f" |📹 1. Kompyuter yonish payti parol so'ramaydigan qilib sozlash. Kompyuterga parolsiz kirish!\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 2- dars
@dp.message_handler(text="Windows zaruriy 2 - dars")
async def windowszarikki(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Kompyuterdan_biror_dasturni_butunlay_o'chirib_yuborish_ortiqcha.mp4",
        "rb")
    txt = f" |📹 2. Kompyuterdan biror dasturni butunlay o'chirib yuborish (ortiqcha dasturlar o'rnatmagan holda)\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Windows zaruriy 3 - dars")
async def windowszaruch(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Kompyuterda_fayl_kengaytmasini_ko'rinadigan_yoki_ko'rinmaydigan.mp4",
        "rb")
    txt = f" |📹 3. Kompyuterda fayl kengaytmasini ko'rinadigan yoki ko'rinmaydigan qilib sozlash\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Windows zaruriy 4 - dars")
async def windowszartort(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Antivirusni_ESET_NOD32_vaqtincha_o'chirib_turish_o'yin_payti,_torrent.mp4",
        "rb")
    txt = f" |📹 4. Antivirusni (ESET NOD32) vaqtincha o'chirib turish (o'yin payti, torrent va b)\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Windows zaruriy 5 - dars")
async def windowszarbesh(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Kompyuterda_sichqonchani_bir_bosganda_kiradigan_qilib_sozlash.mp4",
        "rb")
    txt = f" |📹 5. Kompyuterda sichqonchani bir bosganda kiradigan qilib sozlash\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6- dars
@dp.message_handler(text="Windows zaruriy 6 - dars")
async def windowszarolti(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Kompyuterda_sichqonchani_sezgirligini_oshirish_yoki_kamaytirish.mp4",
        "rb")
    txt = f" |📹 6. Kompyuterda sichqonchani sezgirligini oshirish yoki kamaytirish\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 7- dars
@dp.message_handler(text="Windows zaruriy 7 - dars")
async def windowszaryetti(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/Windows ga parol o'rnatish va olib tashlash.mp4",
        "rb")
    txt = f" |📹 7. Windows ga parol o'rnatish va olib tashlash\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 8- dars
@dp.message_handler(text="Windows zaruriy 8 - dars")
async def windowszaryetti(msg: Message):
    video = open(
        "video/Kampyuter savod/Windows zaruriy sozlamalar/_Предупреждение_системы_безопасности__yoki__Security_warning__ni.mp4",
        "rb")
    txt = f" |📹 8. 'Предупреждение системы безопасности' yoki 'Security warning' ni o'chirish!\n" \
          f"\n Telegram: @Kompyuter_akademiyasi" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga 🖥 ")
async def windzarorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuWindowszaruriy)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Microsoft
@dp.message_handler(text="🧾Microsoft office darslari")
async def microsoft(msg: Message):
    txt = f"Quyidigilarni tanlang!"
    await msg.answer(txt, reply_markup=menuMicrosoftoffice)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#menuExcel
@dp.message_handler(text="Excel dars")
async def excel(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuExcel)

# 1- dars
@dp.message_handler(text="Excel 1 - dars")
async def excelbir(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 1-dars.  Kirish qismi.mp4",
        "rb")
    txt = f" |Excel 1-dars. Kirish !\n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Excel 2 - dars")
async def excelikki(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 2-dars. Jadval va grafik tuzish.mp4",
        "rb")
    txt = f" | EXCEL 2-dars. Jadval va grafik tuzish!\n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Excel 3 - dars")
async def exceluch(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 3-dars. Cell bilan ishlash.mp4",
        "rb")
    txt = f" |EXCEL 3-dars. Cell bilan ishlash\n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Excel 4 - dars")
async def exceltort(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 4-dars. Sonlarni farmatlash.mp4",
        "rb")
    txt = f" |EXCEL 4-dars. Sonlarni farmatlash \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Excel 5 - dars")
async def excelbesh(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 5-dars. Worksheet bilan ishlash.mp4",
        "rb")
    txt = f" |EXCEL 5-dars. Worksheet bilan ishlash \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 6- dars
@dp.message_handler(text="Excel 6 - dars")
async def excelolti(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 6-dars. Ma`lumotdan nusxa olish va ko`chirish.mp4",
        "rb")
    txt = f" |EXCEL 6-dars. Malumotdan nusxa olish va kochirish \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Excel 7 - dars")
async def excelyetti(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 7-dars. Qator va satirlada ishlash.mp4",
        "rb")
    txt = f" |EXCEL 7-dars. Qator va satirlada ishlash \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 8- dars
@dp.message_handler(text="Excel 8 - dars")
async def excelsakkiz(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 8-dars. Jadval bilan ishlash.mp4",
        "rb")
    txt = f" |EXCEL 8-dars. Jadval bilan ishlash  \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 9- dars
@dp.message_handler(text="Excel 9 - dars")
async def exceltoqqiz(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 9-dars. Jadvalda ishlashning  davomi.mp4",
        "rb")
    txt = f" |EXCEL 9-dars. Jadvalda ishlashning  davomi  \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10- dars
@dp.message_handler(text="Excel 10 - dars")
async def excelon(msg: Message):
    video = open(
        "video/Microsoft office/Excel dars/EXCEL 10-dars. Table davomi.mp4",
        "rb")
    txt = f" |EXCEL 10-dars. Table davomi  \n" \
          f"\n YouTube:  https://bit.ly/3fhRwCy" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga📕")
async def exelorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuMicrosoftoffice)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#menuPowerpoint
@dp.message_handler(text="Power point")
async def powerpoint(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuPowerpoint)

# 1- dars
@dp.message_handler(text="Power point 1dars")
async def powerpbir(msg: Message):
    video = open(
        "video/Microsoft office/Power point/PowerPoint kursi 1-dars (T  Ma'ruf).mp4",
        "rb")
    txt = f" |PowerPoint kursi 1-dars (T  Ma'ruf)  !\n Telegram -- @ITmaktabUZ \n" \
          f"\nYouTube:  http://bit.ly/3tLMnGT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Power point 2dars")
async def powerpikki(msg: Message):
    video = open(
        "video/Microsoft office/Power point/PowerPoint_kursi_2_dars__Буфер_обмена__va__слайды__panellari.mp4",
        "rb")
    txt = f" |PowerPoint_kursi_2_dars__Буфер_обмена__va__слайды__panellari.mp4!\n Telegram -- @ITmaktabUZ \n" \
          f"\nYouTube:  http://bit.ly/3tLMnGT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Power point 3dars")
async def powerpuch(msg: Message):
    video = open(
        "video/Microsoft office/Power point/PowerPoint kursi 3-dars _Шрифты_ paneli.mp4",
        "rb")
    txt = f" |PowerPoint kursi 3-dars 'Шрифты' paneli!\n Telegram -- @ITmaktabUZ \n" \
          f"\nYouTube:  http://bit.ly/3tLMnGT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Power point 4dars")
async def powerptort(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slaydlar aro o'tish xillari Perexodlar (T. Ma'ruf).mp4",
        "rb")
    txt = f" | 4-dars: Slaydlar aro o'tish xillari Perexodlar (T. Ma'ruf)!\n Telegram -- @ITmaktabUZ \n" \
          f"\nYouTube:  http://bit.ly/3tLMnGT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Power point 5dars")
async def powerpbesh(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slaydga musiqa qo'yish fonga (T. Ma'ruf).mp4",
        "rb")
    txt = f" | 5-dars:  Slaydga musiqa qo'yish fonga (T. Ma'ruf)" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Power point 6dars")
async def powerpolti(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slayd_PowerPoint_uchun_Idea_yoki_Chiroyli_g'oya_T_Ma'ruf.mp4",
        "rb")
    txt = f" |6-dars: Slayd (PowerPoint) uchun Idea yoki Chiroyli g'oya (T  Ma'ruf) (T. Ma'ruf)" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Power point 7dars")
async def powerpyetti(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slaydga kitobdan rasm qo'yish (T. Ma'ruf).mp4",
        "rb")
    txt = f" |7-dars: Slaydga kitobdan rasm qo'yish (T. Ma'ruf)" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 8- dars
@dp.message_handler(text="Power point 8dars")
async def powerpsakkiz(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slayd hajmini kamaytirish (T. Ma'ruf).mp4",
        "rb")
    txt = f" |8-dars:  Slayd hajmini kamaytirish (T. Ma'ruf) " \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 9- dars
@dp.message_handler(text="Power point 9dars")
async def powerptoqiz(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slayddagi obektlarga animatsiya qo'yish (T. Ma'ruf).mp4",
        "rb")
    txt = f" |9-dars: Slayddagi obektlarga animatsiya qo'yish (T. Ma'ruf) " \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10- dars
@dp.message_handler(text="Power point 10dars")
async def powerpon(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slaydga ovoz joylashtirish (T. Ma'ruf).mp4",
        "rb")
    txt = f" | 10-dars: Slaydga ovoz joylashtirish (T. Ma'ruf) ) " \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 11- dars
@dp.message_handler(text="Power point 11dars")
async def poweronbir(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Slaydga tanlash animatsiyasi qo'yish (T. Ma'ruf).mp4",
        "rb")
    txt = f" |11-dars: Slaydga tanlash animatsiyasi qo'yish (T. Ma'ruf) " \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 12- dars
@dp.message_handler(text="Power point 12dars")
async def poweronbirikki(msg: Message):
    video = open(
        "video/Microsoft office/Power point/Tema yaratish (T. Ma'ruf).mp4",
        "rb")
    txt = f" |12-dars: Tema yaratish (T. Ma'ruf) " \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course"
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga📗")
async def pwerpoorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuMicrosoftoffice)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)




#menuWord
@dp.message_handler(text="Word excel")
async def word(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuWord)

# 1- dars
@dp.message_handler(text="Word 1 - dars")
async def wordbir(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_1_dars_Dastur_bilan_tanishuv_Asosiy_sozlamalar_Qo'shimcha.mp4",
        "rb")
    txt = f" |Word 1-dars. Dastur bilan tanishuv. Asosiy sozlamalar. Qo'shimcha kengaytmalar o'rnatish.!" \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Word 2 - dars")
async def wordikki(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_2_dars_Matnlar_bilan_ishlash__Файл__va__Главная_.mp4",
        "rb")
    txt = f" |Word 2-dars. Matnlar bilan ishlash. 'Файл' va 'Главная' bo'limlari bilan ishlash!!" \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Word 3 - dars")
async def worduch(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_2_dars__Вставка__bo'limi_Rasmlar_bilan_ishlash_.mp4",
        "rb")
    txt = f" |Word 3-dars. 'Вставка' bo'limi. Rasmlar bilan ishlash.!" \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Word 4 - dars")
async def wordtort(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_4_dars_Jadvallar_bilan_ishlash_Formula_terish_.mp4",
        "rb")
    txt = f" |Word 4-dars. Jadvallar bilan ishlash. Formula terish.!" \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Word 5 - dars")
async def wordbesh(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_5_dars__Дизайн_,__Макет_,__Вид__bo'limlari_bilan.mp4",
        "rb")
    txt = f" |Word 5-dars. 'Дизайн', 'Макет', 'Вид' bo'limlari bilan ishlash!" \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Word 6 - dars")
async def wordolti(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_6_dars_Havolalar_bilan_ishlash_Ichki_va_tashqi_havolalar.mp4",
        "rb")
    txt = f" |Word 6-dars. Havolalar bilan ishlash. Ichki va tashqi havolalar." \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Word 7 - dars")
async def wordyetti(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_7_dars_Xavfsizlik_Hujjatni_tahrirlashdan_himoyalash.mp4",
        "rb")
    txt = f" |Word 7-dars. Xavfsizlik. Hujjatlarni tahrirlashdan himoyalash. Saqlanmagan hujjatlarni tiklash." \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="Word 8 - dars")
async def wordsakkiz(msg: Message):
    video = open(
        "video/Microsoft office/Word dars/Microsoft_Word_8_dars_Yakuniy_dars_Word_dasturi_bo'yicha_layfhaxlar.mp4",
        "rb")
    txt = f" |Word 8-dars. Yakuniy dars. Word dasturi bo'yicha layfhaklar. Oson usulda mundarija yaratish." \
          f"\n Telegram -- @Kompyuter_akademiyasi \n" \
          f"\nYouTube: http://bit.ly/3rMfyrT" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga📘")
async def wordorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuMicrosoftoffice)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#3d model
@dp.message_handler(text="🖼3D Model")
async def dmodel(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menu3dmax)

#asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#3d max
@dp.message_handler(text="3D max")
async def max(msg: Message):
    await msg.answer(f"Quyidagilarni tanlang", reply_markup=menuMax)

# 1- dars
@dp.message_handler(text="3D max 1 dars")
async def maxbir(msg: Message):
    video = open(
        "video/3D model/3D max/#1 3Ds Max _ VIEWPORT lar bilan tanishish _ UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 1-dars | VIEWPORT lar bilan tanishish!" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="3D max 2 dars")
async def maxikki(msg: Message):
    video = open(
        "video/3D model/3D max/#2 3Ds Max _ INTERFEYS qismini sozlash _ UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 2-dars | INTERFEYS qismini sozlash!" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="3D max 3 dars")
async def maxuch(msg: Message):
    video = open(
        "video/3D model/3D max/#3 3Ds Max _ PRIMITIVE elementlarni hosil qilish _ UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 3-dars | PRIMITIVE elementlarni hosil qilish" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="3D max 4 dars")
async def maxtort(msg: Message):
    video = open(
        "video/3D model/3D max/#4 3Ds Max _ SELECT, MOVE, ROTATE, SCALE _ UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 4-dars | SELECT, MOVE, ROTATE, SCALE" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="3D max 5 dars")
async def maxbesh(msg: Message):
    video = open(
        "video/3D model/3D max/#5 3Ds Max _ SELECT, MOVE, ROTATE, SCALE (2-qism) _ UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 5-dars | SELECT, MOVE, ROTATE, SCALE (2-qism)" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="3D max 6 dars")
async def maxolti(msg: Message):
    video = open(
        "video/3D model/3D max/#6_3Ds_Max_UNDO,_REDO_va_AUTOBACK_Orqaga,_Oldinga_va_Autoback_UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 6-dars | UNDO, REDO va AUTOBACK (Orqaga, Oldinga va Autoback)" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="3D max 7 dars")
async def maxyetti(msg: Message):
    video = open(
        "video/3D model/3D max/#7 3Ds Max I SAVE (faylni saqlash) turlari I UPDATE.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 7-dars | SAVE (faylni saqlash) turlari" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="3D max 8 dars")
async def maxsakkiz(msg: Message):
    video = open(
        "video/3D model/3D max/#8 3Ds Max COPY I INSTANCE I REFERENCE I Update.mp4",
        "rb")
    txt = f" |3Ds Max darslari | 8-dars | COPY I INSTANCE I REFERENCE" \
          f"\n Telegram -- @inagamov3d \n" \
          f"\nYouTube: http://www.youtube.com/c/Inagamov3D" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga🌄")
async def maxorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menu3dmax)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#Auto cad
@dp.message_handler(text="Autokat")
async def autocad(msg: Message):
    await msg.answer(f"Quyidagilarni tanlang", reply_markup=menuAutocad)

# 1- dars
@dp.message_handler(text="Autocad 1 dars")
async def autocadbir(msg: Message):
    video = open(
        "video/3D model/Autocad/#1_AutoCAD_ўзбек_тилида_видеодарслик_1_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 1-dars!" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Autocad 2 dars")
async def autocadikki(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_1_1_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 2-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Autocad 3 dars")
async def autocaduch(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_2_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 3-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Autocad 4 dars")
async def autocadtort(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_3_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 4-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 5- dars
@dp.message_handler(text="Autocad 5 dars")
async def autocadbesh(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_4_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 5-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Autocad 6 dars")
async def autocadolti(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_5_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 6-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Autocad 7 dars")
async def autocadyetti(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_6_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 7-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="Autocad 8 dars")
async def autocadsakiz(msg: Message):
    video = open(
        "video/3D model/Autocad/AutoCAD_ўзбек_тилида_видеодарслик_7_дарс.mp4",
        "rb")
    txt = f" |AutoCAD darslari | 8-dars" \
          f"\n"\
          f"\nYouTube: http://www.youtube.com/channel/UCkiOUM0qxbFA1CVLYeikFBw" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga🌠")
async def autocadqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menu3dmax)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Smm marketing
@dp.message_handler(text="🏞SMM Marketing")
async def smmmarket(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuSMM)

 # asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#Google ads
@dp.message_handler(text="Google Ads")
async def googleads(msg: Message):
    await msg.answer(f"Quyidagilarni tanlang", reply_markup=menuGoogle)

# 1- dars
@dp.message_handler(text="Google ads 1dars")
async def googlebir(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/1_Google_ads_ro'yhatdan_o'tish_Googleda_reklama_berish_Google_ads.mp4",
        "rb")
    txt = f" |Google Ads darslari | 1-dars | Google ads ro'yhatdan o'tish" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Google ads 2dars")
async def googleikki(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/2_Google_ads_Boshlang’ich_bilimlari_Google_reklama_berishni_o'rganamiz.mp4",
        "rb")
    txt = f" |Google Ads darslari | 2-dars | Google reklama berishni o'rganamiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Google ads 3dars")
async def googleuch(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/3. Google darslari _ Saytni tahlil qilish.mp4",
        "rb")
    txt = f" |Google Ads darslari | 3-dars | Saytni tahlil qilish" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Google ads 4dars")
async def googletort(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/4_Googleda_reklama_berish_Maqsadlarni_aniqlashni_o'rganamiz.mp4",
        "rb")
    txt = f" |Google Ads darslari | 4-dars | Maqsadlarni aniqlashni o'rganamiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Google ads 5dars")
async def googlebesh(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/5. Google ads darslari _ Kalit so'zlarni topish.mp4",
        "rb")
    txt = f" |Google Ads darslari | 5-dars | Kalit so'zlarni topish" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Google ads 6dars")
async def googleolti(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/6. Google qidiruv tizimida reklama joylashtirish.mp4",
        "rb")
    txt = f" |Google Ads darslari | 6-dars | Google qidiruv tizimida reklama joylashtirish" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Google ads 7dars")
async def googleyetti(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/7. Google qidiruv tizimida reklama joylashtirish 2 dars.mp4",
        "rb")
    txt = f" |Google Ads darslari | 7-dars | Google qidiruv tizimida reklama joylashtirish (2)" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="Google ads 8dars")
async def googlesakkiz(msg: Message):
    video = open(
        "video/SMM marketing/Google Ads darslari/8. Youtube reklama nastroykasi _ Video reklama.mp4",
        "rb")
    txt = f" |Google Ads darslari | 8-dars | Youtube reklama nastroyka" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga📲")
async def googleorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuSMM)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Smm insta
@dp.message_handler(text="SMM(instag)")
async def smminsta(msg: Message):
    await msg.answer(f"Quyidagilarni tanlang", reply_markup=menuSmm)

# 1- dars
@dp.message_handler(text="Smm 1dars")
async def smminstabir(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/1. Instagramda profil ochishni o'rganamiz.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 1-dars | Profil ochishni o'rganamiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Smm 2dars")
async def smminstaikki(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/2. Instagram Professional account qilishni o'rganamiz.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 2-dars | Professional account qilishni o'rganamiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Smm 3dars")
async def smminstauch(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/3. Instagramda пост қўйишни ўрганамиз.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 3-dars | Post qo'yishni o'rganamiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Smm 4dars")
async def smminstatort(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/4_Instagram_реклама_настройкаси_Таргетинг.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 4-dars | Targeting" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Smm 5dars")
async def smminstabesh(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/5. Instagram Statistikasini ko'ramiz.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 5-dars | Instagram statistikasini ko'ramiz" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 6- dars
@dp.message_handler(text="Smm 6dars")
async def smminstaolti(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/6_Instagramda_reklama_tuzish_Трафик_instagram_Smm_darslari.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 6-dars | Instagramda reklama tuzish" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Smm 7dars")
async def smminstayetti(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/7_Instagramda_reklama_tuzish_Продвигать_страницу_Instagram.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 7-dars | Instagramda reklama tuzish (2)" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)





# 8- dars
@dp.message_handler(text="Smm 8dars")
async def smminstasakiz(msg: Message):
    video = open(
        "video/SMM marketing/SMM(Insta)/8_Instagramda_reklama_tuzish_Instagram_Direct_Message_smm_kurslari.mp4",
        "rb")
    txt = f" |SMM (Instagram) darslari | 8-dars | nstagram Direct Message" \
          f"\n Telegram -- @mirpolat_tv \n" \
          f"\nYouTube: http://www.youtube.com/c/MirpolatTV" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# back
@dp.message_handler(text="⬅Orqaga📱")
async def smminstaorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuSMM)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#Videomantaj
@dp.message_handler(text="🎥Video montaj")
async def videomantaj(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuVideomantaj)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#After effect
@dp.message_handler(text="Premiere Pro")
async def premierepro(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuPremierepro)

# 1- dars
@dp.message_handler(text="Premiere pro 1dars")
async def premierbir(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/1_DARS_AFTER_EFFECTS_INTERFEYSI_BILAN_TANISHISH_VA_KOMPOZITSIYA.mp4",
        "rb")
    txt = f" | 1-DARS AFTER EFFECTS INTERFEYSI BILAN TANISHISH VA KOMPOZITSIYA YARATISH" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Premiere pro 2dars")
async def premierikki(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/2-DARS AFTER EFFECTS ASBOBLAR PANELI.mp4",
        "rb")
    txt = f" | 2-DARS AFTER EFFECTS ASBOBLAR PANELI" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 3- dars
@dp.message_handler(text="Premiere pro 3dars")
async def premieruch(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/3-DARS AFTER EFFECTS ANIMATSIYA, SCALE, ROTATION, OPACITY.mp4",
        "rb")
    txt = f" | 3-DARS AFTER EFFECTS ANIMATSIYA, SCALE, ROTATION, OPACITY" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Premiere pro 4dars")
async def premiertort(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/4-DARS AFTER EFFECTS  TEXTNI TO'G'RI TAHRIRLASH.mp4",
        "rb")
    txt = f" | 4-DARS AFTER EFFECTS  TEXTNI TO'G'RI TAHRIRLASH" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Premiere pro 5dars")
async def premierbesh(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/5-DARS AFTER EFFETCS SHAPE LAYER VA MASKA YARATISH.mp4",
        "rb")
    txt = f" | 5-DARS AFTER EFFETCS SHAPE LAYER VA MASKA YARATISH" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 6- dars
@dp.message_handler(text="Premiere pro 6dars")
async def premierolti(msg: Message):
    video = open(
        "video/Video Mantaj/After Effect/6-DARS AFTER EFFECTS 3D TEXT YARATISH.mp4",
        "rb")
    txt = f" | 6-DARS AFTER EFFECTS 3D TEXT YARATISH" \
          f"\n Telegram -- @afterpremiere \n" \
          f"\nYouTube: http://bit.ly/3svcaCU" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# back
@dp.message_handler(text="⬅Orqaga📹")
async def premierorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuVideomantaj)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Filmore
@dp.message_handler(text="Filmora")
async def filmore(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuFilmora)

# 1- dars
@dp.message_handler(text="Filmora 1 dars")
async def filmorebir(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#01_FILMORA_ZO'RU_Dasturni_o'rnatish,_qayerdan_olish_va_turli_effektlar.mp4",
        "rb")
    txt = f" |#01 FILMORA ZO'RU Dasturni o'rnatish, qayerdan olish va turli effektlar | video montaj o'zbek tilida" \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Filmora 2 dars")
async def filmoreikki(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#02_FILMORA_ZO'RU_Dastur_bilan_tanishuv,_sozlamalar____video_montaj.mp4",
        "rb")
    txt = f" | #02 FILMORA ZO'RU Dastur bilan tanishuv, sozlamalar || video montaj o'zbek tilida" \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3- dars
@dp.message_handler(text="Filmora 3 dars")
async def filmoreuch(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#03_FILMORA_ZO'RU_Timeline_montajni_boshladik_import,_cut____video.mp4",
        "rb")
    txt = f" | #03 FILMORA ZO'RU Timeline montajni boshladik import, cut || video montaj o'zbek tilida" \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Filmora 4 dars")
async def filmoretort(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#04_FILMORA_ZO'RU_Video_perexodlar,_Transitions____video_montaj.mp4",
        "rb")
    txt = f" | #04 FILMORA ZO'RU Video perexodlar, Transitions || video montaj o'zbek tilida" \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Filmora 5 dars")
async def filmorebesh(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#05_FILMORA_ZO'RU_Audio_bilan_ishlash,_AUDIO_EFFECTS____video_montaj.mp4",
        "rb")
    txt = f" | #05 FILMORA ZO'RU Audio bilan ishlash, AUDIO EFFECTS || video montaj o'zbek tilida " \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 6- dars
@dp.message_handler(text="Filmora 6 dars")
async def filmoreolti(msg: Message):
    video = open(
        "video/Video Mantaj/Filmore/#06_FILMORA_ZO'RU_VIDEO_EFFECTS,_Overlays,_Filters____video_montaj.mp4",
        "rb")
    txt = f" | #06 FILMORA ZO'RU VIDEO EFFECTS, Overlays, Filters || video montaj o'zbek tilida " \
          f"\n Telegram -- @yfmuzmedia \n" \
          f"\nYouTube: http://bit.ly/3tOCfgQ" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# back
@dp.message_handler(text="⬅Orqaga 📹")
async def filmoreorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuVideomantaj)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Amazon
@dp.message_handler(text="🚚Amazon FBA")
async def amazon(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuAmazonfba)

#Amazon seller
@dp.message_handler(text="Amazon seller")
async def amazonseller(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuAmazonseller)


# 1- dars
@dp.message_handler(text="Amazon kirish dars")
async def amazonbir(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Online_savdo_qilish_Amazon_FBA_Kirish_wZWo3RrdvfY_136.mp4",
        "rb")
    txt = f" |Online savdo qilish - Amazon FBA || Kirish" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Amazon 1-dars")
async def amazonikki(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_1_dars_Registratsiya_qilish_2btkv5CyHTA_136.mp4",
        "rb")
    txt = f" |Amazon FBA 1-dars || Registratsiya qilish" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3- dars
@dp.message_handler(text="Amazon 2-dars")
async def amazonuch(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_2_dars_Amazondan_mahsulot_topish._4kyhpqhRlnY_136.mp4",
        "rb")
    txt = f" |Amazon FBA 2-dars || Amazondan mahsulot topish." \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 4- dars
@dp.message_handler(text="Amazon 3-dars")
async def amazontort(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_3_dars_Mahsulotni_analiz_qilish._NPwP6x_NaGA_248.mkv",
        "rb")
    txt = f" |Amazon FBA 3-dars || Mahsulotni analiz qilish." \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Amazon 4-dars")
async def amazonbesh(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_4_dars_Mahsulotni_analiz_qilish_2_qism_J_ylCAHKcY_136.mp4",
        "rb")
    txt = f" |Amazon FBA 4-dars || Mahsulotni analiz qilish.2-qism" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 6- dars
@dp.message_handler(text="Amazon 5-dars")
async def amazonolti(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_5_dars_Alibabadan_mahsulot_topish_8dxQ8IXHuGA_136.mp4",
        "rb")
    txt = f" |Amazon FBA 5-dars ||Alibabadan mahsulot topish" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 7 - dars
@dp.message_handler(text="Amazon 6-dars")
async def amazonyetti(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_6_dars_Biz_to_laydigan_pullar_c8_vlezLpOY_136.mp4",
        "rb")
    txt = f" |Amazon FBA 6-dars || Biz to'laydigan pullar" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


#8 dars
@dp.message_handler(text="Amazon 7-dars")
async def amazonsakiz(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_7_dars_Mahsulotni_amazonga_yuklash_5Yz8H2iTeGs_136.mp4",
        "rb")
    txt = f" |Amazon FBA 7-dars || Mahsulotni amazonga yuklash" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9- dars
@dp.message_handler(text="Amazon 8-dars")
async def amazontoqiz(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_8_dars_Bankdan_hisob_raqam_ochish_IiBMVLfb-w8_136.mp4",
        "rb")
    txt = f" |Amazon FBA 8-dars || Bankdan hisob raqam ochish" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10- dars
@dp.message_handler(text="Amazon 9-dars")
async def amazonon(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_9_dars_Payoneer_Registratsiyadan_o_tamiz_vNNtAqMWbpA.mp4",
        "rb")
    txt = f" |Amazon FBA 9-dars || Payoneer Registratsiyadan o'tamiz." \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 11- dars
@dp.message_handler(text="Amazon 10-dars")
async def amazononbir(msg: Message):
    video = open(
        "video/Amazon/Amazon seller/Amazon_FBA_10_dars_Mahsulotga_reklama_berish_foydalari_KE0yvEmayiM.mp4",
        "rb")
    txt = f" |Amazon FBA 10-dars || Mahsulotga reklama berish foydalari" \
          f"\n Telegram -- @ithouse \n" \
          f"\nYouTube: https://youtu.be/2btkv5CyHTA" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



@dp.message_handler(text="⬅Orqaga🚛")
async def amazonorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuAmazonfba)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#1C buxgalter
@dp.message_handler(text="👨🏻‍💻1C Buxgalter")
async def buxgalterC1(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuBuxgalter)

# 1- dars
@dp.message_handler(text="Buxgalter 1 - dars")
async def buxgalbir(msg: Message):
    video = open(
        "video/1C Buxgalter/1С Бухгалтерия дарслиги 1-дарс.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 1-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Buxgalter 2 - dars")
async def buxgalikki(msg: Message):
    video = open(
        "video/1C Buxgalter/2 dars tashkilot nomini dasturga kiritish.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 2-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 3- dars
@dp.message_handler(text="Buxgalter 3 - dars")
async def buxgaluch(msg: Message):
    video = open(
        "video/1C Buxgalter/3 dars tashkilot kodlari va manzilini kiritish.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 3-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4- dars
@dp.message_handler(text="Buxgalter 4 - dars")
async def buxgaltort(msg: Message):
    video = open(
        "video/1C Buxgalter/4 dars tezda o'zlashtirish paneli haqida.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 4-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Buxgalter 5 - dars")
async def buxgalbesh(msg: Message):
    video = open(
        "video/1C Buxgalter/5 dars ish stoli haqida boshlang'ich tushuncha.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 5-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Buxgalter 6 - dars")
async def buxgalolti(msg: Message):
    video = open(
        "video/1C Buxgalter/6_dars_'monitor_buxgaltera'_haqida_boshlang'ich_ma'lumot.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 6-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Buxgalter 7 - dars")
async def buxgayetti(msg: Message):
    video = open(
        "video/1C Buxgalter/7_dars_'otchet_o_rukovoditelya'_raxbar_uchun_xisobot_bo'limi_bilan.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 7-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="Buxgalter 8 - dars")
async def buxgasakkiz(msg: Message):
    video = open(
        "video/1C Buxgalter/8 dars xisob parametrlarini o'rnatish.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 8-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 9 dars
@dp.message_handler(text="Buxgalter 9 - dars")
async def buxgatoqiz(msg: Message):
    video = open(
        "video/1C Buxgalter/10 dars soddalashtirilgan soliq solish tizimi xisob siyosati.mp4",
        "rb")
    txt = f" |1C Bugalteriya darsligi: 9-dars" \
          f"\n Telegram -- @BUXGALTERIYA1C \n" \
          f"\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)





#Kiber xavsizlik
@dp.message_handler(text="📟Kiber Havsizlik")
async def kiberxavsizlik(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuKiberxavsizlik)


# 1- dars
@dp.message_handler(text="Kiber 1 - dars")
async def kiberbir(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #1.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #1 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

#2 dars
@dp.message_handler(text="Kiber 2 - dars")
async def kiberikki(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #2.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #2 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 3- dars
@dp.message_handler(text="Kiber 3 - dars")
async def kiberuch(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #3.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #3 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 4- dars
@dp.message_handler(text="Kiber 4 - dars")
async def kibertort(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #4.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #4 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 5- dars
@dp.message_handler(text="Kiber 5 - dars")
async def kiberbesh(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #5.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #5 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)



# 6- dars
@dp.message_handler(text="Kiber 6 - dars")
async def kiberbesh(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #6.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #6 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 7- dars
@dp.message_handler(text="Kiber 7 - dars")
async def kiberyetti(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #7.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #7 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)




# 8- dars
@dp.message_handler(text="Kiber 8 - dars")
async def kibersakkiz(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #8.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #8 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 9 dars
@dp.message_handler(text="Kiber 9 - dars")
async def kibertoqqiz(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #9.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #9 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)


# 10- dars
@dp.message_handler(text="Kiber 10 - dars")
async def kiberton(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #10.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #10 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)





# 11- dars
@dp.message_handler(text="Kiber 11 - dars")
async def kibertonbir(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #11.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #11 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# 12 dars
@dp.message_handler(text="Kiber 12 - dars")
async def kibertonikki(msg: Message):
    video = open(
        "video/Kiber-xavsizlik/Kiber Havfsizlik Dars #12.mp4",
        "rb")
    txt = f" |📹 Kiber Havfsizlik Dars #12 " \
          f"\n Telegram -- @saudabdulwahed \n" \
          f"\n You tube: http://bit.ly/3C46ntb\n" \
          f"\n@free_lesson_course_bot -- Free lesson course "
    await bot.send_video(msg.chat.id, video, caption=txt, reply_markup=Iks)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#books
@dp.message_handler(text="📚Kitoblar")
async def kitoblar(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuBooks)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#business
@dp.message_handler(text="Bizness")
async def bizness(msg: Message):
    txt = f"Quyidagilarni Tanlang!"
    await msg.answer(txt, reply_markup=menuBusiness)

#kitob business
@dp.message_handler(text="100 Great buisnes")
async def greatbus(msg: Message):
    kitob = open("book/business/100 Great Business Ideas ( PDFDrive ).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)


#kitob business
@dp.message_handler(text="Be smart in evening")
async def besmart(msg: Message):
    kitob = open("book/business/Be_Smart_in_Everything_That_Matters__Finance,_Marriage,_Lifestyle.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)

#kitob business
@dp.message_handler(text="100 Success secrets")
async def successeccret(msg: Message):
    kitob = open("book/business/Blogging_100_Success_Secrets_100_Most_Asked_Questions_on_Building.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)

#kitob business
@dp.message_handler(text="Out of the Shadow")
async def outofshadow(msg: Message):
    kitob = open("book/business/Out_of_the_Shadows__Understanding_Sexual_Addiction_PDFDrive_.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)


#kitob business
@dp.message_handler(text="Rich and Poor dad")
async def richandpoor(msg: Message):
    kitob = open("book/business/Rich Dad Poor Dad.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)

#kitob business
@dp.message_handler(text="Work from home")
async def richandpoor(msg: Message):
    kitob = open("book/business/Work_from_Home__How_to_Make_Money_Working_at_Home_and_Get_the_Most.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(kitob, caption=txt, reply_markup=Iks)



# back
@dp.message_handler(text="⬅Orqaga📚")
async def kitoborqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBooks)


# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#Dasturlash
@dp.message_handler(text="Dasturlash")
async def dasturlash(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuProgram)

# back
@dp.message_handler(text="⬅Orqaga 📚")
async def kitoborqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuBooks)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#Angular
@dp.message_handler(text="Angular")
async def angular(msg: Message):
    txt = f"Quyidagilarni tanlang "
    await msg.answer(txt, reply_markup=menuAngular)

#enterprise
@dp.message_handler(text="Enterpridse Angular")
async def angular(msg: Message):
    program = open("book/Program/angular/enterprise-angular.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)



@dp.message_handler(text="⬅Orqaga📓")
async def angularorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)

#fullstack
@dp.message_handler(text="Full Stack")
async def fullstackbok(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuFullstack)

#full stuack react
@dp.message_handler(text="Full stack React")
async def fullstackreact(msg: Message):
    program = open("book/Program/Full stack/React-Architect_Full-Stack React App Dev.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)


@dp.message_handler(text="⬅Orqaga📔")
async def fullstackorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)



#html\css
@dp.message_handler(text="Html/CSS")
async def htmlcss(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuHtmlcss)

#begincss
@dp.message_handler(text="Beginning Css")
async def begincss(msg: Message):
    program = open("book/Program/html,css/Beginning CSS, Cascading Style Sheets.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#headfirsthtml
@dp.message_handler(text="Head first html5")
async def headfirst(msg: Message):
    program = open("book/Program/html,css/Head First HTML5 Programming.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)


#HTML & CSS course
@dp.message_handler(text="HTML & CSS course")
async def htmlcsscourse(msg: Message):
    program = open("book/Program/html,css/HTML & CSS Crash Course.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)


#HTML5 in action
@dp.message_handler(text="HTML5 in action")
async def htmlaction(msg: Message):
    program = open("book/Program/html,css/HTML5 in Action (2014).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)



#Css in 24hours
@dp.message_handler(text="Css in 24hours")
async def csshours(msg: Message):
    program = open("book/Program/html,css/Sams Teach Yourself CSS in 24 Hours.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)


#Animatsion css
@dp.message_handler(text="Animatsion css")
async def animatsiacss(msg: Message):
    program = open("book/Program/html,css/Transitions and Animations in CSS_ Adding Motion with CSS.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

@dp.message_handler(text="⬅Orqaga 📕 ")
async def javascriptbokor(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#JavaScript Book
@dp.message_handler(text="JavaScript Book")
async def javascrbok(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuJavascriptbook)

#Javascript
@dp.message_handler(text="Javascript")
async def javascriptsb(msg: Message):
    program = open("book/Program/Javascript/Kayl_Poznakomtes-javascript.642675.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#PHP,Mysql, javascript
@dp.message_handler(text="PHP,Mysql, javascript")
async def javaphp(msg: Message):
    program = open("book/Program/Javascript/Learning PHP, MySQL & JavaScript (2021).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Бессерверные JavaScript
@dp.message_handler(text="Бессерверные JavaScript")
async def besserjavacript(msg: Message):
    program = open("book/Program/Javascript/Бессерверные_приложения_на_JavaScript.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#многопоточние Javascript
@dp.message_handler(text="многопоточние Javascript")
async def mnogojavascrip(msg: Message):
    program = open("book/Program/Javascript/Многопоточный Javascript.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Путь к изучению React
@dp.message_handler(text="Путь к изучению React")
async def reactizuv(msg: Message):
    program = open("book/Program/Javascript/Путь к изучению React 2018-.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

@dp.message_handler(text="⬅Orqaga 📕")
async def javascriptbokor(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#Java book
@dp.message_handler(text="Java book")
async def javabook(msg: Message):
    txt = f"Quyidagilarni tanlang"
    await msg.answer(txt, reply_markup=menuJavabook)

#САМОУЧИТЕЛЬ Java
@dp.message_handler(text="САМОУЧИТЕЛЬ Java")
async def javasamouchit(msg: Message):
    program = open("book/Program/Java/doc341468715_475793101.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Java Concurrency in Practice
@dp.message_handler(text="Java Concurrency in Practice")
async def javaconpract(msg: Message):
    program = open("book/Program/Java/Java_Concurrency_in_practice.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Классические задачи Computer Science на языке Java
@dp.message_handler(text="Классические задачи Computer Science на языке Java")
async def klasikjava(msg: Message):
    program = open("book/Program/Java/Klassicheskie_zadachi_Computer_Science_na_yazyke_Java_2022_Kopets.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Java Programming easy step
@dp.message_handler(text="Java Programming easy step")
async def javaeasystep(msg: Message):
    program = open("book/Program/Java/McGrat_M._Java_Programmirovanie_dla_nachinaushih.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#Modern Java in Action
@dp.message_handler(text="Modern Java in Action")
async def modernjava(msg: Message):
    program = open("book/Program/Java/Modern Java in Action - 2nd Edition.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#OpenCv and Java
@dp.message_handler(text="OpenCv and Java")
async def openjava(msg: Message):
    program = open("book/Program/Java/OpenCV и Java.pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course "
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

@dp.message_handler(text="⬅Orqaga 📗")
async def javascriptbokor(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)


#pythonbook
@dp.message_handler(text="Python book")
async def pythonbool(msg: Message):
    txt = f"Quyidagilarni tanlang!"
    await msg.answer(txt, reply_markup=menuPythonbook)

#begin python book
@dp.message_handler(text="Beginning Python(en)")
async def beginpython(msg: Message):
    program =open("book/Program/python/Beginning Python (en).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#core python
@dp.message_handler(text="Core Python applications program")
async def corepython(msg: Message):
    program =open("book/Program/python/Core Python applications programming (en).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#effective python
@dp.message_handler(text="Effective python(en)")
async def effectpython(msg: Message):
    program =open("book/Program/python/Effective Python (en).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#python web
@dp.message_handler(text="Python Web Penetration testing cookbook")
async def webpython(msg: Message):
    program =open("book/Program/python/Python Web Penetration Testing Cookbook (en).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)

#python dlya detey
@dp.message_handler(text="PYTHON ДЛЯ ДЕТЕЙ И РОДИТЕЛЕЙ")
async def deteypython(msg: Message):
    program =open("book/Program/python/Python для детей и родителей (ru).pdf", "rb")
    txt = f"@free_lesson_course_bot -- Free lesson course"
    await msg.answer_document(program, caption=txt, reply_markup=Iks)


#orqaga
@dp.message_handler(text="⬅Orqaga 📗")
async def pybokorqaga(msg: Message):
    await msg.answer(f"⬅Orqaga", reply_markup=menuProgram)

# asosi
@dp.message_handler(text="🔼Asosiy Menyu")
async def asosiy(msg: Message):
    await msg.answer(f"🔼Asosiy Menyu", reply_markup=menuAsosiy)














# back
@dp.message_handler(text="🔙Ortga")
async def programortga(msg: Message):
    await msg.answer(f"🔙Ortga", reply_markup=menuStart)


if __name__ == '__main__':
    executor.start_polling(dp)

