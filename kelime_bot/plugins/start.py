from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Qrubuna At", url=f"http://t.me/SozTapBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿 Sahibim", url="https://t.me/Thagiyevv"),
        InlineKeyboardButton("📣 Resmi Kanal", url="https://t.me/RiyaddBlog"),
    ]
])


START = """
**🔔 Salam, Sözləri düzgün tapma oynuna xoş gəldin..**

➤ Məlumat üçün 👉 /help Vurun. Ayarlar asand və sadədir. 
"""

HELP = """
**📣 Ayarlar Menyusuna Xoş Gəldiniz.**
/oyun - Oyunu başlamaq üçün..
/kec - Üç ədəd keçmə haqqınız mövcüddur. 
/qreytinq - Oyuncular Arasında ki Rəqabət..
/cancel - Oyundan çıxmaq üçün lazım olan əmirdi.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/24txmswdZLq8jrZ88",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/24txmswdZLq8jrZ88",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗😑 Oyun Onsuzda Qrubunuzda Devam Edir ✍🏻 \n Oyunu dayandırmaq üçün /cancel yaza bilərsiniz.")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nSoz Tapma Oyunu Başladı .\n\nUgurlar!", reply_markup=kanal)
        
        oyun[m.chat.id] = {"soz":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['soz'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Söz :   <code>{kelime_list}</code>
💰 Topladığıniz Xal: 1
🔎 Kömək: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın
        """
        await c.send_message(m.chat.id, text)
        
