import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu pler"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
    
import random
from EmikoRobot.events import register
from EmikoRobot import telethn

KAPAN_STRING = ["Besok kali", 
                 "Kalok ga mager", 
                 "Kapan Kapan", 
                 "Nanya Mulu", 
                 "Tahun Depan", 
                 "Kalau ga sabtu ya minggu",
                 "1 Jam lagi",
                 "Mungkin sekarang",
                 "8 Jam lagi",
                 "Sebulan lagi",
                 "Tahun lalu"
                 ]


@register(pattern="^/kapan ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(KAPAN_STRING))

