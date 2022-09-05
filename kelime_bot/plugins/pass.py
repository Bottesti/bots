from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 3:
            oyun[m.chat.id]["kec"] += 1 
            await c.send_message(m.chat.id,f"❗😑 Maksimum 3 keçmə haqqınız var!\n➡️ Söz Uğurla dəyişdirildi !\n✏️ Düzgün Söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Topladığıniz Xal : 1
🔎 Kömək : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅uq: {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın 
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçid Düzgün Keçildi! </code> \n Oyunu Saxlamaq üçün /cancel yazıb dayandıra bilərsiniz ✍🏻**")
    else:
        await m.reply(f"❗ **Qrubunuzda aktiv oyun oynanılır!\n Yeni bir oyuna başlamaq üçün /oyun yazabilərsiniz✍🏻**")
